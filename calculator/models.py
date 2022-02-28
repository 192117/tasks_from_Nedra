from pydantic import BaseModel, validator
from fastapi import Query

class CalcGet(BaseModel):
    '''
        Модель для POST запросов на /calc/{value} .
    '''

    value: str = Query(None)

    @validator('value')
    def check(cls, v):
        if len(v) == 0:
            raise ValueError("It is necessary to send arguments")
        else:
            return v


class CalcPost(BaseModel):
    '''
        Модель для POST запросов на /calc/{value} .
    '''

    value: str

    @validator('value')
    def check(cls, v):
        if len(v) == 0:
            raise ValueError("It is necessary to send arguments")
        else:
            return v


class CalcResponse(BaseModel):
    '''
            Модель ответов сервиса.
        '''
    response: str = ''


class HistoryPost(BaseModel):
    '''
            Модель для POST запросов на /history .
    '''

    limit: int
    status: str

    @validator('limit')
    def check_limit(cls, v):
        if 1 <= v <= 30:
            return v
        else:
            raise ValueError('It should be from 1 to 30')

    @validator('status')
    def check_status(cls, v):
        if v in ['success', 'fail']:
            return v
        else:
            raise ValueError('success or fail')