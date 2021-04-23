# Get the last line of a binary tree
# @author Yichen


def getInitialTeams(bracket):
    if bracket["left"] == None and bracket["right"] == None:
        return [bracket["contents"]]
    else:
        result = []
        bracket_left = bracket["left"]
        bracket_right = bracket["right"]
        result = result + getInitialTeams(bracket_left)
        result = result + getInitialTeams(bracket_right)
    return result

if __name__ == '__main__':
    t1 = {"contents": "United States",
          "left": {"contents": "United States",
                   "left": {"contents": "England",
                            "left": None,
                            "right": None
                            },
                   "right": {"contents": "United States",
                             "left": None,
                             "right": None
                             }
                   },
          "right": {"contents": "Netherlands",
                    "left": {"contents": "Netherlands",
                             "left": None,
                             "right": None
                             },
                    "right": {"contents": "Sweden",
                              "left": None,
                              "right": None
                              }
                    }
          }
    print(getInitialTeams(t1))
