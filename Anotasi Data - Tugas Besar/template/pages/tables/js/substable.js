$(document).ready(function () {
  $('#subscribers-table').DataTable({
    dom: 'Bfrtip',
    buttons: [
      {
        extend: 'csvHtml5',
        text: '<i class="mdi mdi-printer"></i> CSV',
        titleAttr: 'CSV',
        title: 'Subscribers',
        exportOptions: {
          columns: ':not(:last-child)',
        },
      },
    ],
  });
});

$(document).ready(function () {
  $('#subscribers-table1').DataTable({
    dom: 'Bfrtip',
    buttons: [
      {
        extend: 'csvHtml5',
        text: '<i class="mdi mdi-printer"></i> CSV',
        titleAttr: 'CSV',
        title: 'Subscribers',
        exportOptions: {
          columns: ':not(:last-child)',
        },
      },
    ],
  });
});
