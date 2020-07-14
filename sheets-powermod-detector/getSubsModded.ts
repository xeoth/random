const MODSUBS = async (username: string) => {
  const rawResponse = UrlFetchApp.fetch(
    `https://reddit.com/user/${username}/moderated_subreddits.json`,
    { muteHttpExceptions: true }
  );

  const jsonResponse = JSON.parse(rawResponse.getContentText());

  if (jsonResponse.error) {
    return jsonResponse.message;
  }

  return jsonResponse.data ? jsonResponse.data.length : 0;
};
