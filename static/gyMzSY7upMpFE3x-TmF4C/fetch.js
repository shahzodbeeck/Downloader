document.querySelector('.downbtn').addEventListener('click', () => {
    const formData = new FormData();
    const urlValue = document.querySelector('.url_down').value;
    formData.append('url', urlValue);
    const encodedUrl = btoa(urlValue);
    fetch('/convert', {
        method: 'POST',
        body: formData,
        headers: {
            'accept-message': encodedUrl

        }
    })
        .then(response => {
            console.log('Response headers:', response.headers); // Debug: Log response headers
            return response.json();
        })
        .then(data => {
            let add_divs=document.querySelector('.down_center')
           data.forEach((item,index)=>{
              add_divs.innerHTML+=`${item}`
           })
        })
        .catch(error => {
            console.error('Fetch error:', error);
        });
});
