import React, {Component} from 'react'
import {Spinner, Icon, EditableText} from "@blueprintjs/core"
import {gql, graphql} from 'react-apollo';
import moment from 'moment'
import singleQuestion from '../queries/SingleQuestionQuery'

const editCommentMutation = gql`
mutation editCommentMutation($text: String!, $userId: String!, $id: String!) {
    editComment(text: $text, userId: $userId, id: $id) {
        comment {
            id,
            text
        }
        ok
    }
}
`

class Comment extends Component {

  constructor(props) {
    super(props);
    this.state = {
      editable: user.id === props.comment.owner.id,
      editing: false,
      value: props.comment.text,
    };

    this.toggleEdit = this.toggleEdit.bind(this);
    this.handleChange = this.handleChange.bind(this);
    this.saveComment = this.saveComment.bind(this);
  }

  toggleEdit (event) {
    this.setState({
      editing: !this.state.editing
    });
  }

  handleChange(event) {
    this.setState({value: event.target.value});
  }

  saveComment(event) {
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
        id: this.props.comment.id,
        userId: user.id
      }
    })
      .then(({data}) => {
        console.log('got data', data);
        this.toggleEdit();
      })
      .catch((error) => {
        console.log('got error', error);
      });
    event.preventDefault()
  }

  EditingComment(comment) {
    return (
      <form onSubmit={this.saveComment}>
        <div className="pt-input-group">
          <input
            id="editComment"
            onChange={this.handleChange}
            value={this.state.value}
            className="pt-input pt-fill"
            type="text"
            dir="auto"
          />
          <span className="pt-icon pt-icon-cross" onClick={this.toggleEdit}/>
        </div>
      </form>
    )
  }

  ViewingComment(comment) {
    return (
      <div className="commentBlock">
        {comment.text} -
        <small>{comment.owner.getFullName}, {moment(comment.created).calendar()}</small>
        &nbsp;
        {this.state.editable ? <Icon iconName="pt-icon-edit" onClick={this.toggleEdit}/> : ''}
      </div>
    )
  }

  render() {
    const comment = this.props.comment;

    return (
      <div className="comment">
        <div className="commentScore">{comment.score}</div>
        {this.state.editing ?
          this.EditingComment(comment)
        :
          this.ViewingComment(comment)
        }
      </div>
    )
  }

}


export default graphql(editCommentMutation)(Comment)