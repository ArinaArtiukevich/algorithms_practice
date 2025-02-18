from typing import List

import pandas as pd

def createDataframe(student_data: List[List[int]]) -> pd.DataFrame:
    return pd.DataFrame(data=student_data, columns=['student_id', 'age'])

if __name__ == '__main__':
    print(createDataframe(student_data=[
                                            [1, 15],
                                            [2, 11],
                                            [3, 11],
                                            [4, 20]
                                        ]
                            )
    )
