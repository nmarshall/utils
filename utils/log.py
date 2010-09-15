import logging

_loggers = {} 

def get_logger(name = 'default', format = None, level = None):
    '''
    This is a wrapper for the standard logging module provided by python
    The idea is to provide a means of making it flexible to change by extracting the
    settings out of a settings file when needed
    
    TODO: at the moment is ignores the settings file
    '''
    
    global _loggers
    name = str(name)
    
    logger = _loggers.get(name, None)
    if logger is None:
        raw_logger = logging.getLogger(name = name)
        if not raw_logger.handlers:
            setup_logger(format = format, level = level)
        logger = LoggerClass(raw_logger)
        _loggers[name] = logger
    return logger
    
def setup_logger(format = None, level = None):
    if level is None:
        level = logging.DEBUG
    logging.basicConfig(format = format, level = level)

class LoggerClass(object):
    
    def __init__(self, logger):
        self._logger = logger
        self._fns = {}
    
    def _get_fn(self, level):
        fns = self._fns
        fn = fns.get(level, None)
        if fn is None:
            try:
                fn = getattr(self._logger, level)
            except AttributeError, e:
                msg = "Level %s, is not recognised" %level
                raise ValueError(msg)
            fns[level] = fn
        return fn
        
    def log(self, msg, level):
        fn = self._get_fn(level)
        fn(msg)
        
        
        