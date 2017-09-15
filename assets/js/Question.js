import {
  createFragmentContainer,
  graphql
} from 'react-relay'
import React, {Component} from 'react'

class Question extends Component {

  render() {
    return (
      <p>{this.props.question.text}</p>
    )
  }

}

export default createFragmentContainer(Question, graphql`
  fragment Question_question on QuestionNode {
    id
    text
  }
`)