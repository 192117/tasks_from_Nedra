from fastapi import FastAPI, Depends
from models import *
from calc import *

app = FastAPI()

db = []

@app.get('/calc',
          summary='Calc as post method',
          description='Calculates expression {value}.')
async def get_calc(query: CalcGet = Depends(CalcGet)):
    values = query.dict()
    values.setdefault('response', polska(RPN(check_value(values['value']))))
    answer = {
        'request': '',
        'response': '',
        'status': ''
    }
    if '[]' in values['response']:
        answer['request'], answer['response'], answer['status'] = values['value'], '', 'fail'
        if len(db) > 30:
            del db[0]
        db.append(answer)
        return 'Incorrect expression'
    else:
        answer['request'], answer['response'], answer['status'] = values['value'], values['response'], 'success'
        if len(db) >= 30:
            del db[0]
        db.append(answer)
        return values['response']


@app.post('/calc',
          summary='Calc as post method',
          description='Calculates expression {value}.')
async def post_calc(body: CalcPost):
    values = body.dict()
    values.setdefault('response', polska(RPN(check_value(values['value']))))
    answer = {
        'request': '',
        'response': '',
        'status': ''
    }
    if '[]' in values['response']:
        answer['request'], answer['response'], answer['status'] = values['value'], '', 'fail'
        if len(db) >= 30:
            del db[0]
        db.append(answer)
        return 'Incorrect expression'
    else:
        answer['request'], answer['response'], answer['status'] = values['value'], values['response'], 'success'
        if len(db) >= 30:
            del db[0]
        db.append(answer)
        return values['response']


@app.post('/history',
         summary='Shows all requests',
         description='Shows 30 recent requests.')
async def get_history(body: HistoryPost):
    values = body.dict()
    result = []
    n = 0
    if values['status'] == 'success':
        for element in db:
            if element['status'] == values['status']:
                result.append(element)
                n += 1
            if n == values['limit']:
                break
    elif values['status'] == 'fail':
        for element in db:
            if element['status'] == values['status']:
                result.append(element)
                n += 1
            if n == values['limit']:
                break
    return result


@app.get('/history',
         summary='Shows all requests',
         description='Shows 30 recent requests.')
async def get_history():
    return db