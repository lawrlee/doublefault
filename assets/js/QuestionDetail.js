import React, {Component} from 'react'
import {graphql, compose, gql} from 'react-apollo'
import {Spinner, Icon} from "@blueprintjs/core"
import Comment from "./Comment"
import Tags from "./Tags"
import UserBadge from "./UserBadge"

const singleQuestion = gql`
  query Question($id: Int!) {
    question(id: $id) {
      id
      title
      text
      created
      modified
      comments {
        id
        text
        score
        modified
        created
        owner {
          id
          getFullName
        }
      }
      owner {
        id
        getFullName
      }
      score
      answers {
        id
        text
        modified
        created
        owner {
          id
          getFullName
        }
      }
      views
      tags {
        id
        name
      }
    }
  }
`

class Question extends Component {

  render() {

    if (this.props.data.loading) {
      return (
        <div id="loader">
          <Spinner className="pt-large" intent="primary"/>
        </div>
      )
    }

    const question = this.props.data.question;

    return (
      <main>
        <left></left>
        <content>
          <h2>{question.title}</h2>
          <div className="questionDetail">
            <div className="questionScore">
              <h1><Icon iconName="pt-icon-caret-up" iconSize="inherit"/></h1>
              <h3>{question.score}</h3>
              <h1><Icon iconName="pt-icon-caret-down" iconSize="inherit"/></h1>
            </div>
            <div className="questionBlock">
              <div className="questionText">
                <p>{question.text}</p>
              </div>
              <div className="questionTags">
                <Tags tags={question.tags}/>
              </div>
              <div className="questionOwner">
                <UserBadge user={question.owner} created={question.created}/>
              </div>
              <div className="commentBlock">
                {question.comments.map((comment) =>
                  <Comment key={comment.id} comment={comment}/>
                )}
              </div>
            </div>
          </div>
        </content>
        <right></right>
      </main>
    )
  }

}

export default compose(
  graphql(singleQuestion, {
    options: (props) => ({
      variables: {
        id: props.match.params.id
      }
    })
  })
)(Question)