
// create a self invoking arrow function
(() => {
  const debug = false

  if (debug) {
    console.log('\n\n[DEMO] Hi all, lets do some cool things.\n');
    console.log(' Queries:\nWhat is a MID code?\nWhich taxes are written by legislation?\nHow do I email a shipping label?\n----')
  }

  let gnpanel = document.querySelector('.fxg-guidednavigation');
  if(gnpanel) {

    gnpanel.style.backgroundColor = 'rgba(240, 240, 240, 1)';
    
    let htmlTemplate = `
    <div class="filter-nav">
      <input
        type="text" name="q" value=""
        class="cc-aem-c-form__input js-searchbar-input cc-aem-u-bg-color--white"
        aria-label="I'm looking for..."
        autocomplete="off"
        placeholder="I'M LOOKING FOR..."
      />
      <svg class="cc-aem-c-icon cc-aem-u-mr--2 " aria-hidden="true">
        <use href="#brand_search_s" x="0" y="0"></use>
      </svg>
    </div>
    
    <div class="result hidden">
      <h4></h4>
      <p></p>
      <a class="more" target="_blank" href="">Read more</a>
      <a class="showrelevant" href="">Relevant</a>
    </div>

    <div class="relevant hidden">
      <h4>Helpful FAQ's</h4>
      <ul></ul>
    </div>
    `;

    let styleTemplate = `
    <style>
      .filter-nav {
        position: relative;
      }

      .filter-nav > input[type="text"] {
        position: relative;
        padding: 10px 20px;
      }

      .filter-nav .cc-aem-c-icon{
        position: absolute;
        top: 14px;
        right: 10px;
      }

      .result {
        padding: 32px 24px;
        background: #fff;
      }

      .result p{
        margin-bottom: 16px;
      }

      [dir] .relevant{
        padding: 0 24px 32px 24px;
        background: #fff;
      }

      .relevant h4 {
        margin: 0 0 1.5rem 0 !important;
        font-size: 1.2rem;
        font-weight: 400;
      }

      .relevant ul{
        padding-left: 16px;
      }
      .relevant li a{
        font-size: 0.9rem;
        margin-bottom: 6px;
      }

      [dir] .result h4{
        margin: 0 0 24px 0 !important;
      }

      [dir] .result > a.more {
        float:right;
        font-size: 0.875rem;
      }

      [dir] .relevant li > a {
        cursor: pointer;
      }

      [dir] .relevant li > a:hover ~ span.extra-info.hidden{
        display: block !important;
      }

      [dir] .relevant span.extra-info {
        position: absolute;
        margin-top: 10px;
        padding: 12px;
        border: 1px solid #eee;
        border-radius: 3px;
        box-shadow: 0px 2px 4px rgba(0,0,0,.15);
        background: #fff;
        z-index: 10;
        max-width: 50vw;
      }

    </style>
    `;

    let template = document.createElement('template');
    template.innerHTML = htmlTemplate + styleTemplate; 
    gnpanel.prepend(template.content);

    



    function lookupFAQ(query='Who pays duties and taxes?') {
      const els = Array.from(document.querySelectorAll('a.fxg-guidednavigation__link'))
      const filtered = els.filter( (el) => el.innerText.trim() == query);
      let location = undefined;
      if (filtered.length > 0) {
        const fel = filtered[0];
        if (fel) {
          location = fel.getAttribute('href');
        }
      }
      return location 
      
    };

    // create a timeout of 1 ms
    setTimeout(() => {
      if (debug) {
        console.log('[Update] Template is injected.');
      }

      document.querySelector('.fxg-guidednavigation > .result .showrelevant').addEventListener('click', (e) => {
        e.preventDefault();

        document.querySelector('.fxg-guidednavigation > .relevant').classList.toggle('hidden');
      });

      // Wait for rendering of the template
      let inputField = document.querySelector('.filter-nav > input[type="text"]');
      // add a listener for press on Enter key on the inputField
      inputField.addEventListener('keyup', (e) => {
        if (e.keyCode === 13){
          // get the value of the input field
          let filterTerm = e.target.value;

          if (debug) {
            console.log(filterTerm);
          }

          if (filterTerm.length > 8) {
            fetch('http://localhost:8000/filter', {
              method: 'POST',
              headers: {
                'Content-Type': 'application/json'
              },
              body: JSON.stringify({
                query: filterTerm
              })
            }).then(res => res.json())
             .then(data => {
                console.log('Filtered content:', data);

                const top = data.output.top;
                const results = data.output.results;
                
                // Set TOP location
                let location = 'https://www.fedex.com/en-gb/customer-support/contact.html';
                if (top.title) {
                  location = lookupFAQ(top.title) || null;
                }

                // update the results in the DOM by replacing the {{}} placeholders with the results from the backend
                const result = document.querySelector('.fxg-guidednavigation > .result')

                result.classList.remove('hidden');
                result.querySelector('h4').innerHTML = top.title || "We're sorry";
                result.querySelector('p').innerHTML = top.text || "We could not find an FAQ for your question.<br />Please try our <a href='https://www.fedex.com/en-gb/customer-support/contact.html'>contact page</a> for more support.";
                result.querySelector('a').setAttribute('href', location)

                // Set relevant FAQ's
                const relevant = document.querySelector('.fxg-guidednavigation > .relevant');
                let faqListTemplate = ''
                // loop through results and set relevant FAQ's
                for (let i = 0; i < results.length; i++) {
                  const resultItem = document.createElement('li');
                  resultLocation = lookupFAQ(results[i].title) || null;

                  title = `<a>${results[i].title}</a>`;
                  if (resultLocation) {
                    title = `<a href='${results[i].url}' target='_blank'>${results[i].title}</a>`
                  }
                  faqListTemplate += `<li>${title}<span class="extra-info hidden">${results[i].text}</span></li>`;
                }

                relevant.querySelector('ul').innerHTML = faqListTemplate;

             }).catch(err => {
                console.error('Error:', err);
             });
          } else {
            console.warn('- Please enter a something real to filter on.');
          }
        }
      });


    }, 1);
  }

})();