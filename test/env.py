import sys
from os import path
# Add me2gpx to python path so tests
# can import the code they need to exercise.
package_path = path.abspath(
                    path.dirname(
                        path.dirname(__file__)
                    )
              )

sys.path.append(package_path)
