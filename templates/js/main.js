const postlist = document.querySelector('.posts-list');
const addPostForm = document.querySelector('.add-post-form')
const titleValue = document.getElementById('title-value')
const bodyValue = document.getElementById('body-value')
const btnSubmit = document.querySelector('.btn')


console.log(btnSubmit.value)

let output = '';

const renderPosts = (posts) => {
    posts.forEach(post => {
        output += `
            <div class="card mt-4 col-md-6 bg-light">
                <div class="card-body" data-id=${post.blog_id}>
                <h5 class="card-title">${post.title}</h5>
                <h6 class="card-subtitle mb-2 text-muted">${post.datetime}</h6>
                <p class="card-text">${post.body}</p>
                <a href="#" class="card-link" id="blog_edit">Edit</a>
                <a href="#" class="card-link" id="blog_delete" >Delete</a>
                </div>
            </div>
        `;
    });
    postlist.innerHTML = output;
}

const urlGet = 'http://127.0.0.1:5000/getBlogs';
const urlAdd = 'http://127.0.0.1:5000/addBlog';
const urlDel = 'http://127.0.0.1:5000/deleteBlog';
const urlEdit = 'http://127.0.0.1:5000/editBlog';
// Get - Read the posts
// Method - Get
fetch(urlGet)
    .then(res => res.json())
    .then(data => {renderPosts(data)})


postlist.addEventListener('click',(e)=>{
    e.preventDefault()
    let delButtonIsPressed = e.target.id == 'blog_delete';
    let editButtonIsPressed = e.target.id == 'blog_edit';

    let id = e.target.parentElement.dataset.id
    //Delete remove a post
    //method Delete
    if(delButtonIsPressed){
        fetch(`${urlDel}/${id}`,{
            method: 'DELETE'
        })
        .then(res => res.json())
        .then(() => location.reload())
    }

    if(editButtonIsPressed){
        const parent = e.target.parentElement;
        let titleContent = parent.querySelector('.card-title').textContent;
        let bodyContent = parent.querySelector('.card-text').textContent;

        titleValue.value = titleContent;
        bodyValue.value = bodyContent;
    }    
    // on button press
    // method fetch
    btnSubmit.addEventListener('click', (e) => {
        e.preventDefault()
        fetch(urlEdit,{
            method : 'patch',
            headers :  {'Content-Type': 'application/json'},
            body : JSON.stringify({
                title : titleValue.value,
                body : bodyValue.value,
                blog_id : String(id),
            })
        }).then(res => res.json())
        .then(() => location.reload())
    })
    // reset the values    
    
})

// POST - add new blog
// method - Post
addPostForm.addEventListener('submit', (e)=>{
    e.preventDefault()
    fetch(urlAdd, {
        method : 'post',
        headers : {
            'Content-Type': 'application/json'
        },
        body : JSON.stringify({
            title : titleValue.value,
            body : bodyValue.value,  
        })
    })
    .then(res => res.json())
    .then(data =>(renderPosts(data)))

    // reset the values 
    titleValue.value = '';
    bodyValue.value = '';
})