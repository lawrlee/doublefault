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
      <table style={{tableLayout: 'fixed'}}>
        <tbody>
        <tr>
          <td style={{width: '260px'}}>
            <div style={{display: 'flex'}}>
              <div className="pt-card" style={{textAlign: 'center'}}>
                <h5>{question.score}</h5>
                <span className="pt-text-muted">Votes</span>
              </div>
              <div className="pt-card" style={{textAlign: 'center'}}>
                <h5>{question.answers.length}</h5>
                <span className="pt-text-muted">Answers</span>
              </div>
              <div className="pt-card" style={{textAlign: 'center'}}>
                <h5>{question.views}</h5>
                <span className="pt-text-muted">Views</span>
              </div>
            </div>
          </td>
          <td style={{width: '100%'}}>
            <table style={{width: '100%'}}>
              <tbody>
              <tr>
                <td><h5>{question.title}</h5></td>
              </tr>
              <tr>
                <td>
                  <blockquote className="pt-text-overflow-ellipsis">
                    {question.text}
                  </blockquote>
                </td>
              </tr>
              <tr>
                <td>{question.tags.map((tag) =>
                  <Tag key={tag.id} className="pt-tag pt-minimal pt-intent-primary">{tag.name}</Tag>)
                }
                </td>
              </tr>
              <tr>
                <td style={{textAlign: 'right'}}>
                  asked {moment(question.created).fromNow()} - {question.owner.getFullName}&nbsp;
                  <Icon iconName="pt-icon-person"/>
                </td>
              </tr>
              </tbody>
            </table>
          </td>
        </tr>
        </tbody>
      </table>
    )
  }

}

export default compose(
  graphql(allQuestions, {name: 'allQuestionsQuery'})
)(QuestionList)