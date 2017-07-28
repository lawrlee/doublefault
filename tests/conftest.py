import pytest

from graphene.test import Client
from django.core.management import call_command

from web.schema import schema


@pytest.fixture(scope='session')
def django_db_setup(django_db_setup, django_db_blocker):
    with django_db_blocker.unblock():
        call_command('loaddata', 'tests/test_fixtures.json')


@pytest.fixture(scope='session')
def client():
    return Client(schema)


@pytest.fixture
def all_question_query_result(db, client):
    return client.execute(
        '''
{
  allQuestions {
    edges {
      node {
        id
        owner {
          id
        }
      }
    }
  } 
}
        '''
    )


@pytest.fixture
def all_answer_query_result(db, client):
    return client.execute(
        '''
{
  allAnswers {
    edges {
      node {
        id
        owner {
          id
        }
      }
    }
  } 
}
        '''
    )


@pytest.fixture
def all_comment_query_result(db, client):
    return client.execute(
        '''
{
  allComments {
    edges {
      node {
        id
        owner {
          id
        }
      }
    }
  } 
}
        '''
    )


@pytest.fixture
def all_tag_query_result(db, client):
    return client.execute(
        '''
{
  allTags {
    edges {
      node {
        id
      }
    }
  } 
}
        '''
    )


@pytest.fixture
def all_user_query_result(db, client):
    return client.execute(
        '''
{
  allUsers {
    edges {
      node {
        id
      }
    }
  } 
}
        '''
    )
