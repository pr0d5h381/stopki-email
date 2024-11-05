class SignatureTemplate:
    @staticmethod
    def generate_html(data):
        html_template = f'''
<div>
    <style>
        .sh-src a {{
            text-decoration: none !important;
        }}
    </style>
</div>
<br>
<table cellpadding="0" cellspacing="0" border="0" class="sh-src" style="">
    <tr>
        <td style="padding: 0px 1px 0px 0px;">
            <table cellpadding="0" cellspacing="0" border="0" style="border-collapse: separate;">
                <tr>
                    <td align="center" valign="top" style="padding: 0px 25px 0px 0px; vertical-align: top;">
                        <table cellpadding="0" cellspacing="0" border="0" style="">
                            <tr>
                                <td style="padding: 0px 1px 0px 0px;">
                                    <p style="margin: 1px;">
                                        <img src="{data['profile_image']}" 
                                             alt="" 
                                             style="display: block; border: 0px; width: auto; height: 100px; max-width: 100px; object-fit: contain;">
                                    </p>
                                </td>
                            </tr>
                        </table>
                    </td>
                    <td valign="top" style="padding: 0px 30px 0px 1px; vertical-align: top;">
                        <table cellpadding="0" cellspacing="0" border="0" style="">
                            <tr>
                                <td style="padding: 0px 1px 0px 0px; font-family: Arial, sans-serif; font-size: 13px; line-height: 16px; white-space: nowrap;">
                                    <p style="font-family: Arial, sans-serif; font-size: 19px; line-height: 25px; font-weight: 700; color: rgb(0,0,0); white-space: nowrap; margin: 1px;">{data['name']}</p>
                                    <p style="font-family: Arial, sans-serif; font-size: 13px; line-height: 17px; white-space: nowrap; color: rgb(121,121,121); margin: 1px;">{data['position']}</p>
                                    <p style="font-family: Arial, sans-serif; font-size: 13px; line-height: 17px; white-space: nowrap; color: rgb(121,121,121); margin: 1px;">{data['department']}</p>
                                </td>
                            </tr>
                        </table>
                    </td>
                    <td style="padding: 1px 0px 0px; border-right: 1px solid rgb(248,173,37);"></td>
                    <td valign="top" style="padding: 0px 1px 0px 30px; vertical-align: top;">
                        <table cellpadding="0" cellspacing="0" border="0" style="">
                            <tr>
                                <td style="padding: 0px 1px 0px 0px;">
                                    <table cellpadding="0" cellspacing="0" border="0" style="">
                                        <tr>
                                            <td valign="middle" style="padding: 1px 5px 1px 0px; vertical-align: middle;">
                                                <p style="margin: 1px;">
                                                    <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="icon icon-tabler icons-tabler-outline icon-tabler-mail"><path stroke="none" d="M0 0h24v24H0z" fill="none"/><path d="M3 7a2 2 0 0 1 2 -2h14a2 2 0 0 1 2 2v10a2 2 0 0 1 -2 2h-14a2 2 0 0 1 -2 -2v-10z" /><path d="M3 7l9 6l9 -6" /></svg>
                                                </p>
                                            </td>
                                            <td style="line-height: 16px; padding: 1px 0px; vertical-align: middle;">
                                                <p style="margin: 1px;">
                                                    <a href="mailto:{data['email']}" style="font-family: Arial, sans-serif; font-size: 13px; line-height: 16px; white-space: nowrap; color: rgb(121,121,121); text-decoration: none !important;">
                                                        <span style="font-family: Arial, sans-serif; font-size: 13px; line-height: 16px; white-space: nowrap; color: rgb(121,121,121); text-decoration: none !important;">{data['email']}</span>
                                                    </a>
                                                </p>
                                            </td>
                                        </tr>
                                        <tr>
                                            <td valign="middle" style="padding: 1px 5px 1px 0px; vertical-align: middle;">
                                                <p style="margin: 1px;">
                                                    <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="icon icon-tabler icons-tabler-outline icon-tabler-phone"><path stroke="none" d="M0 0h24v24H0z" fill="none"/><path d="M5 4h4l2 5l-2.5 1.5a11 11 0 0 0 5 5l1.5 -2.5l5 2v4a2 2 0 0 1 -2 2a16 16 0 0 1 -15 -15a2 2 0 0 1 2 -2" /></svg>
                                                </p>
                                            </td>
                                            <td style="line-height: 16px; padding: 1px 0px; vertical-align: middle;">
                                                <p style="margin: 1px;">
                                                    <a href="tel:{data['phone']}" style="font-family: Arial, sans-serif; font-size: 13px; line-height: 16px; white-space: nowrap; color: rgb(121,121,121); text-decoration: none !important;">
                                                        <span style="font-family: Arial, sans-serif; font-size: 13px; line-height: 16px; white-space: nowrap; color: rgb(121,121,121); text-decoration: none !important;">{data['phone']}</span>
                                                    </a>
                                                </p>
                                            </td>
                                        </tr>
                                        <tr>
                                            <td valign="middle" style="padding: 1px 5px 1px 0px; vertical-align: middle;">
                                                <p style="margin: 1px;">
                                                    <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="icon icon-tabler icons-tabler-outline icon-tabler-map-pin"><path stroke="none" d="M0 0h24v24H0z" fill="none"/><path d="M9 11a3 3 0 1 0 6 0a3 3 0 0 0 -6 0" /><path d="M17.657 16.657l-4.243 4.243a2 2 0 0 1 -2.827 0l-4.244 -4.243a8 8 0 1 1 11.314 0z" /></svg>
                                                </p>
                                            </td>
                                            <td style="line-height: 16px; padding: 1px 0px; vertical-align: middle;">
                                                <p style="margin: 1px;">
                                                    <span style="font-family: Arial, sans-serif; font-size: 13px; line-height: 16px; white-space: nowrap; color: rgb(121,121,121); text-decoration: none !important;">{data['address']}</span>
                                                </p>
                                            </td>
                                        </tr>
                                        <tr>
                                            <td valign="middle" style="padding: 1px 5px 1px 0px; vertical-align: middle;">
                                                <p style="margin: 1px;">
                                                    <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="icon icon-tabler icons-tabler-outline icon-tabler-phone"><path stroke="none" d="M0 0h24v24H0z" fill="none"/><path d="M9 15l6 -6" /><path d="M11 6l.463 -.536a5 5 0 0 1 7.071 7.072l-.534 .464" /><path d="M13 18l-.397 .534a5.068 5.068 0 0 1 -7.127 0a4.972 4.972 0 0 1 0 -7.071l.524 -.463" /></svg>
                                                </p>
                                            </td>
                                            <td style="line-height: 16px; padding: 1px 0px; vertical-align: middle;">
                                                <p style="margin: 1px;">
                                                    <a href="{data['website']}" style="font-family: Arial, sans-serif; font-size: 13px; line-height: 16px; white-space: nowrap; color: rgb(121,121,121); text-decoration: none !important;">
                                                        <span style="font-family: Arial, sans-serif; font-size: 13px; line-height: 16px; white-space: nowrap; color: rgb(121,121,121); text-decoration: none !important;">{data['website'].replace('https://', '')}</span>
                                                    </a>
                                                </p>
                                            </td>
                                        </tr>
                                        <tr>
                                            <td colspan="2" style="padding: 15px 0px 15px 0px;">
                                                <table cellpadding="0" cellspacing="0" border="0" style="">
                                                    <tr>
                                                        <td style="padding: 0px 10px 0px 0px;">
                                                            <a href="{data['facebook']}">
                                                                <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#F8AD25" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="icon icon-tabler icons-tabler-outline icon-tabler-brand-facebook"><path stroke="none" d="M0 0h24v24H0z" fill="none"/><path d="M7 10v4h3v7h4v-7h3l1 -4h-4v-2a1 1 0 0 1 1 -1h3v-4h-3a5 5 0 0 0 -5 5v2h-3" /></svg>
                                                            </a>
                                                        </td>
                                                        <td style="padding: 0px 10px 0px 0px;">
                                                            <a href="{data['linkedin']}">
                                                                <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#F8AD25" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="icon icon-tabler icons-tabler-outline icon-tabler-brand-linkedin"><path stroke="none" d="M0 0h24v24H0z" fill="none"/><path d="M8 11v5" /><path d="M8 8v.01" /><path d="M12 16v-5" /><path d="M16 16v-3a2 2 0 1 0 -4 0" /><path d="M3 7a4 4 0 0 1 4 -4h10a4 4 0 0 1 4 4v10a4 4 0 0 1 -4 4h-10a4 4 0 0 1 -4 -4z" /></svg>
                                                            </a>
                                                        </td>
                                                        <td style="padding: 0px 10px 0px 0px;">
                                                            <a href="{data['instagram']}">
                                                                <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#F8AD25" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="icon icon-tabler icons-tabler-outline icon-tabler-brand-instagram"><path stroke="none" d="M0 0h24v24H0z" fill="none"/><path d="M4 8a4 4 0 0 1 4 -4h8a4 4 0 0 1 4 4v8a4 4 0 0 1 -4 4h-8a4 4 0 0 1 -4 -4z" /><path d="M9 12a3 3 0 1 0 6 0a3 3 0 0 0 -6 0" /><path d="M16.5 7.5v.01" /></svg>
                                                            </a>
                                                        </td>
                                                        <td style="padding: 0px 10px 0px 0px;">
                                                            <a href="{data['youtube']}">
                                                                <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#F8AD25" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="icon icon-tabler icons-tabler-outline icon-tabler-brand-youtube"><path stroke="none" d="M0 0h24v24H0z" fill="none"/><path d="M2 8a4 4 0 0 1 4 -4h12a4 4 0 0 1 4 4v8a4 4 0 0 1 -4 4h-12a4 4 0 0 1 -4 -4v-8z" /><path d="M10 9l5 3l-5 3z" /></svg>
                                                            </a>
                                                        </td>
                                                    </tr>
                                                </table>
                                            </td>
                                        </tr>
                                    </table>
                                </td>
                            </tr>
                        </table>
                    </td>
                </tr>
            </table>
        </td>
    </tr>
    <tr>
        <td style="padding: 30px 1px 0px 0px;">
            <table cellpadding="0" cellspacing="0" border="0" style="">
                <tr>
                    <td style="padding: 0px 0px 0px 0px;">
                        <table cellpadding="0" cellspacing="0" border="0" style="">
                            <tr>
                                <td style="padding: 0px 0px 0px 0px;">
                                    <p style="margin: 0px;">
                                        <a href="https://www.podnosniki.pl/">
                                            <img src="https://podnosniki.pl/wp-content/uploads/2024/11/Logo-stopka.png" 
                                                 alt="" 
                                                 width="200"
                                                 height="200" 
                                                 style="display: block; border: 0px; width: 200px; height: 200px;">
                                        </a>
                                    </p>
                                </td>
                                <td style="padding: 0px 0px 0px 0px;">
                                    <p style="margin: 0px;">
                                        <a href="https://www.podnosniki.pl/">
                                            <img src="https://podnosniki.pl/wp-content/uploads/2024/11/Banner-stopka.png" 
                                                 alt="" 
                                                 width="400"
                                                 height="200" 
                                                 style="display: block; border: 0px; width: 400px; height: 200px;">
                                        </a>
                                    </p>
                                </td>
                            </tr>
                        </table>
                    </td>
                </tr>
            </table>
        </td>
    </tr>
    <tr>
        <td style="padding: 0px 1px 0px 0px;">
            <table cellpadding="0" cellspacing="0" border="0" style="max-width: 600px;">
                <tr>
                    <td style="padding: 30px 1px 0px 0px; font-family: Arial, sans-serif; font-size: 10px; line-height: 13px; color: rgb(136,136,136);">
                        <p style="font-family: Arial, sans-serif; font-size: 10px; line-height: 13px; color: rgb(136,136,136); margin: 1px;">{data['disclaimer']}</p>
                    </td>
                </tr>
            </table>
        </td>
    </tr>
</table>
'''
        return html_template
