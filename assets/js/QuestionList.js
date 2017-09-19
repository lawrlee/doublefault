import {graphql, compose, gql} from 'react-apollo'
import React, {Component} from 'react'
import {Icon, Spinner, Tag} from "@blueprintjs/core";
import moment from 'moment';

const allQuestions = gql`
  query allQuestions {
    allQuestions {
      id
      title
      text
      created
      owner { 
        getFullName
      }
      score
      answers {
        id
      }
      views
      tags {
        id
        name
      }
    }
  }
`

class QuestionList extends Component {

  render() {
    if (this.props.allQuestionsQuery.loading) {
      return <Spinner className="pt-large" intent="primary"/>
    }

    const questions = this.props.allQuestionsQuery.allQuestions;

    return (
      <main>
        <left></left>
        <content>
          {questions.map((question) =>
            <QuestionItem key={question.id} question={question}/>
          )}
        </content>
        <right></right>
      </main>
    )
  }
}

class QuestionItem extends Component {

  render() {
    const question = this.props.question;

    return (
      <div id="questionItem">
        <div id="votesAnswersViews">
          <div className="pt-card">
            <h5>{question.score}</h5>
            <span className="pt-text-muted">Votes</span>
          </div>
          <div className="pt-card">
            <h5>{question.answers.length}</h5>
            <span className="pt-text-muted">Answers</span>
          </div>
          <div className="pt-card">
            <h5>{question.views}</h5>
            <span className="pt-text-muted">Views</span>
          </div>
        </div>
        <div id="questionSummary">
          <div>
            <h5>{question.title}</h5>
            <blockquote className="pt-text-overflow-ellipsis">
              {question.text}
            </blockquote>
          </div>
          <div id="tagsAndOwner">
            <div id="questionTags">
              {question.tags.map((tag) =>
                <Tag key={tag.id} className="pt-tag pt-minimal pt-intent-primary">{tag.name}</Tag>)
              }
            </div>
            <div id="questionOwner">
              asked {moment(question.created).fromNow()} - {question.owner.getFullName}&nbsp;<Icon
              iconName="pt-icon-person"/>
            </div>
          </div>
        </div>
      </div>
    )
  }

}

export default compose(
  graphql(allQuestions, {name: 'allQuestionsQuery'})
)(QuestionList)