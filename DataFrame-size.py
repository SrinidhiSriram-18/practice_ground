import pandas as pd

def getDataframeSize(players: pd.DataFrame) -> List[int]:
    val=players.shape
    return(list(val))