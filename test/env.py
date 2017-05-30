import sys
from os import path

package_path = path.abspath(
                    path.dirname(
                        path.dirname(__file__)
                    )
              )

sys.path.append(package_path)
