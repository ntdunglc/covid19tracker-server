from fastapi import FastAPI

app = FastAPI()


@app.get("/traces/{timestamp}/{lat}/{long}")
def get_traces(timestamp: int, lat:float, long:float):
    return [{'ts':1584066182,'lat':32.769306,'long':32.769306},
            {'ts':1584066181,'lat':32.769450,'long':-96.779751}
            ]