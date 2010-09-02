from bound import bound
__all__ = ['linear',
           'prev_point',]
class interpolation_base(object):
  def __init__(self, abscissae, ordinates):
    if not sorted(abscissae) or \
         len(abscissae) != len(ordinates):
      raise ValueError, 'abscissae/ordinates length mismatch'
    self.N = len(abscissae)
    self.abscissae, self.ordinates = abscissae, ordinates

  def locate(self, x):
    i, j = bound(x, self.abscissae)
    x_lo, x_hi = self.abscissae[i], self.abscissae[j]
    y_lo, y_hi = self.ordinates[i], self.ordinates[j]

    return (i, j, x_lo, x_hi, y_lo, y_hi)
    
class linear(interpolation_base):
    def __init__(self, abscissae, ordinates):
        interpolation_base.__init__(self, abscissae, ordinates)

    def __call__(self, x):
        i, j, x_lo, x_hi, y_lo, y_hi = interpolation_base.locate(self, x)
    
        if x_hi == x_lo:
            return y_hi
       
        R = 1.0 - (x_hi - x)/(x_hi - x_lo)

        return R*(y_hi - y_lo) + y_lo

class prev_point(interpolation_base):
    def __call__(self, x):
        i, j, x_lo, x_hi, y_lo, y_hi = interpolation_base.locate(self, x)
    
        if x_hi == x_lo:
            return y_hi
        else:
            return y_lo
        