<html>
    <head>
        <style type="text/css">
            ${css}
        </style>
    </head>
    <body>
        %for o in objects :
            <table width = '100%' class='td_company_title'>
                <tr>
                    <td style="vertical-align: top;max-height: 45px;">
                        ${helper.embed_image('jpeg',str(o.company_id.logo),180, 85)}
                    </td>
                    <td>
                    <div>
                        ${o.company_id.name or ''|entity}</div>
                        <br>${o.company_id.partner_id.street or ''|entity} No.
                        ${o.company_id.partner_id.street2 or ''|entity}
                        ${o.company_id.partner_id.zip or ''|entity}<br/>
                        ${o.company_id.partner_id.city or ''|entity},
                        ${o.company_id.partner_id.state_id.name or ''|entity},
                        ${o.company_id.partner_id.country_id.name or ''|entity}
                    </td>
                </tr>
            </table>
         %endfor
    </body>
</html>
