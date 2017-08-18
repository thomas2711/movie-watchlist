// constructs the suggestion engine
var movies = new Bloodhound({
    datumTokenizer: Bloodhound.tokenizers.whitespace,
    queryTokenizer: Bloodhound.tokenizers.whitespace,
    local: movies_typeahead
  });
  
  $('#bloodhound .typeahead').typeahead({
    hint: true,
    highlight: true,
    minLength: 1
  },
  {
    name: 'movies',
    source: movies
  });

  $('.typeahead').bind('typeahead:select', function(ev, suggestion) {
    console.log('Selection: ' + suggestion);
    window.location.href = pks[movies_typeahead.indexOf(suggestion)];
  });