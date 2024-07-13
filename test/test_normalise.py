import pytest
import numpy as np

def normalize(X):
  print("normalize", X, X.min(),X.max())
  print("X-Xmin", X-X.min())
  print("/n resultado", (X - X.min())/(X.max() - X.min()))
  return (X - X.min())/(X.max() - X.min())

#first we generate a long ser of settings 
# settings = []
# for x in [1, 2, 30]:
#   for y in [1, 2, 30]:
#     settings.append((x,y))
#Next, we place them in parametrize 
# for item in settings:
#   print(item)
#   X = np.random.normal((item[0], item[1]))
#   X_norm = normalize(X)
#   print('shapeX',X.shape)
#   print('shapeXnorm', X_norm.shape)

@pytest.mark.parametrize("x",[1, 2, 30])
@pytest.mark.parametrize("y", [1, 2, 30])
def test_shape_same(x,y):
  if x == y:
    pytest.skip('Not of interest')
  X = np.random.normal((x,y))
  X_norm = normalize(X)
  assert X.shape == X_norm.shape    