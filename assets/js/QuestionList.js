import {graphql, compose, gql} from 'react-apollo'
import React, {Component} from 'react'
import {Link} from 'react-router-dom'
import {Icon, Spinner, Tag} from "@blueprintjs/core"
import moment from 'moment'
import allQuestions from '../queries/AllQuestionsQuery'


class QuestionList extends Component {

  render() {
    if (this.props.allQuestionsQuery.loading) {
      return (
        <div id="loader">
          <Spinner className="pt-large" intent="primary"/>
        </div>
      )
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
      <div className="questionItem">
        <div className="votesAnswersViews">
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
        <div className="questionSummary">
          <div>
            <h5><Link to={'/question/' + question.id}>{question.title}</Link></h5>
            <blockquote className="pt-text-overflow-ellipsis">
              {question.text}
            </blockquote>
          </div>
          <div className="tagsAndOwner">
            <div className="questionTags">
              {question.tags.map((tag) =>
                <Tag key={tag.id} className="pt-tag pt-minimal pt-intent-primary">{tag.name}</Tag>)
              }
            </div>
            <div className="questionOwner">
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