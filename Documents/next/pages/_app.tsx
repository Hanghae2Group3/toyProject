import { ApolloProvider } from '@apollo/client';
import NavBar from '@components/NavBar';
import NoteInput from '@components/NoteInput';
import NoteList from '@components/NoteList';
import createApolloClient from '@graphql/createApolloClient';

const client = createApolloClient;

const App = ({ Component, pageProps }) => {
  return (
    <>
      <ApolloProvider client={client}>
        <NavBar />
        <NoteList />
        <NoteInput />
        <Component {...pageProps} />
      </ApolloProvider>
    </>
  );
};

export default App;

// 렌더링 하기전에 이 파일을 먼저 본다.
// 모든 페이지는 _app.tsx 파일을 통한다.
// 글로벌 CSS 이파일에 선언
