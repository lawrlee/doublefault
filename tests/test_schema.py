import pytest

from graphene.test import Client

from web.schema import schema

@pytest.fixture(scope='session')
def client():
    return Client(schema)

@pytest.mark.django_db(transaction=False)
def test_get_all_questions(client):
    executed = client.execute(
        '''
{
  allQuestionPosts {
    id
  } 
}
        '''
    )
    assert 'allQuestionPosts' in executed['data']
    assert len(executed['data']['allQuestionPosts']) == 1