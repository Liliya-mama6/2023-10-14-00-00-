from fastapi import APIRouter


router1=APIRouter(prefix='/user', tags=['user'])


@router1.get('/')
def all_users():
    pass


@router1.get('/user_id')
def user_by_id():
    pass


@router1.post('/create')
def create_user():
    pass


@router1.put('/update')
def update_user():
    pass


@router1.delete('/delete')
def delete_user():
    pass
