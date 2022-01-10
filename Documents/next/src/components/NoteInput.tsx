import { useMutation } from '@apollo/client';
import { ADD_NOTE } from '@graphql/mutations';
import { GET_NOTES } from '@graphql/queries';
import { useState } from 'react';

const NoteInput = () => {
  const [content, setContent] = useState('');
  const [addNote, { loading, error }] = useMutation(ADD_NOTE, {
    update(cache, { data: { addNote } }) {
      const { notes } = cache.readQuery({ query: GET_NOTES });
      cache.writeQuery({
        query: GET_NOTES,
        data: { notes: [...notes, addNote] },
      });
    },
    onCompleted({ addNote: { id } }) {
      alert(`노트가 추가되었습니다. (ID: ${id})`);
    },
  });

  const handleClick = () => {
    addNote({ variables: { content } });
    setContent('');
  };
  return (
    <>
      <input
        value={content}
        onChange={({ target: { value } }) => setContent(value)}
        placeholder="new note"
        disabled={loading}
      />
      <button onClick={handleClick} disabled={loading}>
        추가
      </button>
    </>
  );
};

export default NoteInput;
