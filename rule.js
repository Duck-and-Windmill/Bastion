module.exports = {
  summary: 'a rule to modify response',
  *beforeSendResponse(requestDetail, responseDetail) {
    console.dir(requestDetail);
    return new Promise((resolve, reject) => {
      resolve({ response: responseDetail.response });
    });
  },
};