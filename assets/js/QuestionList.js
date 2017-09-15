import {
  createFragmentContainer,
  graphql
} from 'react-relay'
import React, {Component} from 'react'
import Question from './Question'

// const mockQuestionData = [
//   {
//     node: {
//       id: "1",
//       text: "Howdy Partner"
//     }
//   },
//   {
//     node: {
//       id: "2",
//       text: "Ice Cream!"
//     }
//   }
// ]

class QuestionList extends Component {

  render() {
    const questions = this.props.questions.allQuestions;
    return (
      <div className="alert alert-success" role="alert">
        {questions.edges.map(({node}) =>
          <Question key={node.id} question={node}/>
        )}
      </div>
    )
  }
}


export default createFragmentContainer(QuestionList, graphql`
  fragment QuestionList_questions on QuestionNodeConnection {
    edges {
      node {
        ...Question_question
      }
    }
  }
`)