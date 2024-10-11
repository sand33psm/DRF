api_url = 'http://127.0.0.1:8000/book/'


book_container = document.querySelector('.books')

data = fetch(api_url).then(response => response.json())
.then(book_data=>{
    if (book_data){
        console.log(book_data)
        for (let i = 0; i < book_data.length; i++) {
            render_book(book_data[i])            
          }
    }
})


function render_book(book){
    
    book_container.innerHTML += `
        <div class="book">
            <h2>${book.title}</h2>
            <h2>${book.author}</h2>
            <h2>${book.created_at}</h2>
        </div>
    `
}