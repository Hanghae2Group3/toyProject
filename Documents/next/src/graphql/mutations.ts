import { gql } from '@apollo/client';

export const ADD_NOTE = gql`
  mutation addNotes($content: String) {
    addNote(content: $content) {
      id
      content
    }
  }
`;
