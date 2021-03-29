// TODO Allow for custom sentences. Let the user say something
//  then type it in via <audio></audio> playback

function newSentence() {
    fetch('https://example.com/profile/avatar', {
      method: 'GET',
    })
    .then(response => response.json())
    .then(result => {
      console.log('Success:', result);
    })
    .catch(error => {
      console.error('Error:', error);
    });
}

function uploadAudio() {
    const formData = new FormData();
    const fileField = document.querySelector('input[type="file"]');

    formData.append('sentence', 'abc123');
    formData.append('file', fileField.files[0]);
    fetch('https://example.com/profile/avatar', {
      method: 'POST',
      body: formData
    })
    .then(response => response.json())
    .then(result => {
      console.log('Success:', result);
    })
    .catch(error => {
      console.error('Error:', error);
    });
}
