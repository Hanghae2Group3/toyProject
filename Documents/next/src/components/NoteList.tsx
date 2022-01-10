import { useQuery } from '@apollo/client';
import { GET_NOTES } from '@graphql/queries';

const NoteList = () => {
  const { loading, error, data } = useQuery(GET_NOTES);
  if (loading) return <p>로딩 중...</p>;
  if (error) return <p>오류 :(</p>;
  const { notes } = data;

  return (
    <div>
      <ul>
        {notes.map(({ id, content }) => (
          <li key={id}>{content}</li>
        ))}
      </ul>
    </div>
  );
};

export default NoteList;
