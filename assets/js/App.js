import {
  QueryRenderer,
  graphql
} from 'react-relay'
import environment from './Environment'
import React, {Component} from 'react'
import QuestionList from './QuestionList'

const AppAllQuestionQuery = graphql`
  query AppAllQuestionsQuery {
    questions {
      ...QuestionList_questions
    }
  }
`

class App extends Component {
  render() {
    return (
      <QueryRenderer
        environment={environment}
        query={AppAllQuestionQuery}
        render={({error, props}) => {
          if (error) {
            return <div>{error.message}</div>
          } else if (props) {
            return <QuestionList questions={props.questions}/>
          }
          return <div>Loading</div>
        }}
      />
    )
  }
}

export default App;
