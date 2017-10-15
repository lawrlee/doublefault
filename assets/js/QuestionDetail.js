import React, {Component} from 'react'
import {graphql, compose, gql} from 'react-apollo'
import {Spinner, Icon} from "@blueprintjs/core"
import Comment from "./Comment"
import Tags from "./Tags"
import UserBadge from "./UserBadge"
import AddComment from "./AddComment"
import singleQuestion from "../queries/SingleQuestionQuery"


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
                  <Comment key={comment.id} comment={comment} questionId={question.id}/>
                )}
                <AddComment answerId={''} questionId={question.id} ownerId={user.id} />
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