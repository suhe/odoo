<html>
    <head>
        <style>
            ${css}
        </style>
    </head>
    <body>
     %for o in objects:
        <table class="table table-striped">
            <tbody>
                <tr>
                    <th>Employee</th>
                    <td>${o.employee_id.name}</td>
                </tr>
            </body>
        </table>
     %endfor
    </body>
</html>