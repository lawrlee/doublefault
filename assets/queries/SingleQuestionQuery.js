import {gql} from 'react-apollo';

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

export default singleQuestion