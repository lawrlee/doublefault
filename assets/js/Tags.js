import React, {Component} from 'react'
import {Spinner, Icon, Tag} from "@blueprintjs/core"

class Tags extends Component {

  render() {
    const tags = this.props.tags;

    return (
      <span>
        {tags.map((tag) =>
          <Tag className="pt-large" key={tag.id}>{tag.name}</Tag>
        )}
      </span>
    )
  }

}

export default Tags;