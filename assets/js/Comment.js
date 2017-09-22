import React, {Component} from 'react'
import {Spinner, Icon} from "@blueprintjs/core"
import moment from 'moment'

class CommentBlock extends Component {

  render() {
    const comments = this.props.comment;

    return (
      <div></div>
    )
  }

}

class Comment extends Component {

  render() {
    const comment = this.props.comment;

    return (
      <div className="comment">
        <div className="commentScore">{comment.score}</div>
        <div className="commentBody">
          {comment.text} - {comment.owner.getFullName} {moment(comment.created).format('ll')}
        </div>
      </div>
    )
  }

}

export default Comment;