from django.db import connection
from django.http import JsonResponse

def contracted_biz_view(request, *args, **kwargs):
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT 
                biz.section_id_id AS SectionId,
                biz.line_biz_id_id AS LineBizId,
                biz.id,
                biz.name,
                s.name AS SectionName,
                lb.name AS LineBizName
            FROM m_lineareacontractedbiz biz
            JOIN m_section s ON s.id = biz.section_id_id
            JOIN m_linebiz lb ON lb.id = biz.line_biz_id_id
            JOIN m_lineareaaccessauthorization auth ON biz.id = auth.line_area_contracted_biz_id_id
            JOIN m_organization o ON auth.organization_code_id = o.organization_code
            JOIN m_userorgpositionmgmt u ON u.organization_code_id = o.organization_code
            WHERE 
                biz.is_deleted = 0 
                AND s.is_deleted = 0 
                AND lb.is_deleted = 0 
                AND auth.is_deleted = 0 
                AND o.is_deleted = 0 
                AND u.is_deleted = 0 
                AND u.user_no_id = %s
        """, [1])
        columns = [col[0] for col in cursor.description]
        results = [dict(zip(columns, row)) for row in cursor.fetchall()]

    return JsonResponse(results, safe=False)
