import pytest


def _create_post_mutation(mutation, query, input):
    return '''
mutation MyMutation {{
  {mutation}(input: {input}) {{
    {query} {{
      id
      text
      owner {{
        id
      }}
      upvotes {{
        id
      }}
      downvotes {{
        id
      }}
      score
    }}
  }}
}}
'''.format(mutation=mutation, query=query, input=input)


def _get_all_query(query):
    return '''
{{
  {query} {{
    edges {{
      node {{
        id
        owner {{
          id
        }}
      }}
    }}
  }} 
}}
'''.format(query=query)


@pytest.mark.django_db(transaction=False)
def test_create_question(client, all_user_query_result, snapshot):
    user_id = all_user_query_result['data']['allUsers']['edges'][0]['node']['id']
    input = '{{text: "creating a question", ownerId: "{user_id}"}}'.format(user_id=user_id)
    result = client.execute(_create_post_mutation('createQuestion', 'question', input))
    snapshot.assert_match(result)


@pytest.mark.django_db(transaction=False)
def test_create_answer(client, all_user_query_result, all_question_query_result, snapshot):
    user_id = all_user_query_result['data']['allUsers']['edges'][0]['node']['id']
    question_id = all_question_query_result['data']['allQuestions']['edges'][0]['node']['id']
    input = '{{text: "creating an answer", ownerId: "{user_id}", questionId: "{question_id}"}}'.format(user_id=user_id,
                                                                                                       question_id=question_id)
    result = client.execute(_create_post_mutation('createAnswer', 'answer', input))
    snapshot.assert_match(result)


@pytest.mark.django_db(transaction=False)
def test_create_comment_for_answer(client, all_user_query_result, all_answer_query_result, snapshot):
    user_id = all_user_query_result['data']['allUsers']['edges'][0]['node']['id']
    answer_id = all_answer_query_result['data']['allAnswers']['edges'][0]['node']['id']
    input = '{{text: "creating a comment", ownerId: "{user_id}", answerId: "{answer_id}"}}'.format(user_id=user_id,
                                                                                                   answer_id=answer_id)
    result = client.execute(_create_post_mutation('createComment', 'comment', input))
    snapshot.assert_match(result)


@pytest.mark.django_db(transaction=False)
def test_create_comment_for_question(client, all_user_query_result, all_question_query_result, snapshot):
    user_id = all_user_query_result['data']['allUsers']['edges'][0]['node']['id']
    question_id = all_question_query_result['data']['allQuestions']['edges'][0]['node']['id']
    input = '{{text: "creating a comment", ownerId: "{user_id}", questionId: "{question_id}"}}'.format(user_id=user_id,
                                                                                                       question_id=question_id)
    result = client.execute(_create_post_mutation('createComment', 'comment', input))
    snapshot.assert_match(result)


@pytest.mark.django_db(transaction=False)
@pytest.mark.parametrize('mutation,mutation_field,query,', [
    ('editQuestion', 'question', 'allQuestions'),
    ('editAnswer', 'answer', 'allAnswers'),
    ('editComment', 'comment', 'allComments'),
])
@pytest.mark.parametrize('wrong_user', [True, False])
def test_edit(client,
              mutation,
              mutation_field,
              query,
              all_user_query_result,
              wrong_user,
              snapshot):
    post = client.execute(_get_all_query(query))['data'][query]['edges'][0]
    post_id = post['node']['id']
    post_owner_id = post['node']['owner']['id']
    # choose a different user if wrong_user==True, this edit should fail
    if wrong_user:
        post_owner_id = [x['node']['id'] for x in all_user_query_result['data']['allUsers']['edges'] if
                         not x['node']['id'] == post_owner_id][0]
    input = '{{text: "made an edit" {mutation_field}Id: "{post_id}", userId: "{user_id}"}}'.format(
        mutation_field=mutation_field,
        post_id=post_id,
        user_id=post_owner_id
    )
    result = client.execute(_create_post_mutation(mutation, mutation_field, input))
    snapshot.assert_match(result)


@pytest.mark.django_db(transaction=False)
@pytest.mark.parametrize('up_or_down', [
    'downvote',
    'upvote',
])
@pytest.mark.parametrize('mutation,mutation_field,query,', [
    ('{}Question', 'question', 'allQuestions'),
    ('{}Answer', 'answer', 'allAnswers'),
    ('{}Comment', 'comment', 'allComments'),
])
def test_voting(client,
                up_or_down,
                mutation,
                mutation_field,
                query,
                all_user_query_result,
                snapshot):
    mutation = mutation.format(up_or_down)
    post = client.execute(_get_all_query(query))['data'][query]['edges'][0]
    post_id = post['node']['id']
    user_id = all_user_query_result['data']['allUsers']['edges'][0]['node']['id']
    input = '{{{mutation_field}Id: "{post_id}", userId: "{user_id}"}}'.format(
        mutation_field=mutation_field,
        post_id=post_id,
        user_id=user_id
    )
    result = client.execute(_create_post_mutation(mutation, mutation_field, input))
    snapshot.assert_match(result)
