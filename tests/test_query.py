import pytest

FULL_QUERY = '''
{
  allQuestions {
    edges {
      node {
        id
        text
        created
        modified
        score
        views
        tags {
          id
        }
        owner {
          id
          username
        }
        upvotes {
          id
        }
        downvotes {
          id
        }
        acceptedAnswer {
          id
        }
        comments {
          id
          text
          owner {
            id
            username
          }
        }
        answers {
          edges {
            node {
              id
              text
              accepted {
                id
              }
              created
              modified
              owner {
                id
                username
              }
              comments {
                id
                text
                owner {
                  id
                  username
                }
              }
            }
          }
        }
      }
    }
  }
  __debug {
    sql {
      rawSql
    }
  }
}
'''


@pytest.mark.django_db(transaction=False)
def test_get_question(client, all_question_query_result):
    question_id = all_question_query_result['data']['allQuestions']['edges'][0]['node']['id']
    executed = client.execute(
        '''
{{
  question(id: "{question_id}") {{
    id
  }} 
}}
        '''.format(question_id=question_id)
    )
    assert 'question' in executed['data']
    assert executed['data']['question']['id'] == question_id


@pytest.mark.django_db(transaction=False)
def test_get_all_questions(all_question_query_result):
    assert 'allQuestions' in all_question_query_result['data']
    assert len(all_question_query_result['data']['allQuestions']['edges']) == 2


@pytest.mark.django_db(transaction=False)
def test_get_answer(client, all_answer_query_result):
    answer_id = all_answer_query_result['data']['allAnswers']['edges'][0]['node']['id']
    executed = client.execute(
        '''
{{
  answer(id: "{answer_id}") {{
    id
  }} 
}}
        '''.format(answer_id=answer_id)
    )
    assert 'answer' in executed['data']
    assert executed['data']['answer']['id'] == answer_id


@pytest.mark.django_db(transaction=False)
def test_get_all_answers(all_answer_query_result):
    assert 'allAnswers' in all_answer_query_result['data']
    assert len(all_answer_query_result['data']['allAnswers']['edges']) == 2


@pytest.mark.django_db(transaction=False)
def test_get_comment(client, all_comment_query_result):
    comment_id = all_comment_query_result['data']['allComments']['edges'][0]['node']['id']
    executed = client.execute(
        '''
{{
  comment(id: "{comment_id}") {{
    id
  }} 
}}
        '''.format(comment_id=comment_id)
    )
    assert 'comment' in executed['data']
    assert executed['data']['comment']['id'] == comment_id


@pytest.mark.django_db(transaction=False)
def test_get_all_comments(all_comment_query_result):
    assert 'allComments' in all_comment_query_result['data']
    assert len(all_comment_query_result['data']['allComments']['edges']) == 4


@pytest.mark.django_db(transaction=False)
def test_get_tag(client, all_tag_query_result):
    tag_id = all_tag_query_result['data']['allTags']['edges'][0]['node']['id']
    executed = client.execute(
        '''
{{
  tag(id: "{tag_id}") {{
    id
  }} 
}}
        '''.format(tag_id=tag_id)
    )
    assert 'tag' in executed['data']
    assert executed['data']['tag']['id'] == tag_id


@pytest.mark.django_db(transaction=False)
def test_get_all_tags(all_tag_query_result):
    assert 'allTags' in all_tag_query_result['data']
    assert len(all_tag_query_result['data']['allTags']['edges']) == 2
