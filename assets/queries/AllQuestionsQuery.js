import {gql} from 'react-apollo';

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

export default allQuestions