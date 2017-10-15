import React, {Component} from 'react';
import PropTypes from 'prop-types';
import {gql, graphql} from 'react-apollo';
import singleQuestion from '../queries/SingleQuestionQuery';


const addCommentMutation = gql`
mutation addCommentMutation($text: String!, $ownerId: String!, $questionId: String!, $answerId: String!) {
    createComment(text: $text, ownerId: $ownerId, questionId: $questionId, answerId: $answerId) {
        comment {
            id,
            text
        }
        ok
    }
}
`

class AddComment extends Component {
  constructor(props) {
    super(props);
    this.state = {
      value: ''
    };

    this.handleChange = this.handleChange.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);
  }

  handleSubmit(event) {
    console.log(this.state.value, this.props);
    this.props.mutate({
      refetchQueries: [{
        query: singleQuestion,
        variables: {
          id: Number(this.props.questionId)
        }
      }],
      variables: {
        text: this.state.value,
        ownerId: this.props.ownerId,
        questionId: this.props.questionId,
        answerId: this.props.answerId,
      }
    })
      .then(({data}) => {
        console.log('got data', data);
        this.setState({value: ''});
      })
      .catch((error) => {
        console.log('got error', error);
      });
    event.preventDefault()
  }

  handleChange(event) {
    this.setState({value: event.target.value});
  }

  render() {

    return (
      <form onSubmit={this.handleSubmit}>
        <input
          id="addComment"
          onChange={this.handleChange}
          value={this.state.value}
          className="pt-input pt-fill"
          type="text"
          placeholder="Add Comment"
          dir="auto"/>
      </form>
    )
  }


}

export default graphql(addCommentMutation)(AddComment)
