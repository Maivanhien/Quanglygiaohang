from django.db import models
from django.contrib.auth.models import User

# Institution Model
class Institution(models.Model):
    institution_code = models.CharField(max_length=50, primary_key=True, null=False)
    institution_name = models.CharField(max_length=200, null=False)
    create_at = models.DateTimeField(auto_now=True)
    create_by = models.IntegerField(default=1)
    is_deleted = models.BooleanField(default=False)

# Organization Model
class Organization(models.Model):
    organization_code = models.CharField(max_length=50, primary_key=True, null=False)
    level = models.IntegerField(default=1)
    parent_organization = models.ForeignKey('self', on_delete=models.SET_NULL, null=True)
    organization_name = models.CharField(max_length=200, null=False)
    institution_code = models.ForeignKey(Institution, on_delete=models.SET_NULL, null=True)
    sort_order = models.IntegerField(default=1)
    create_at = models.DateTimeField(auto_now=True)
    create_by = models.IntegerField(default=1)
    is_deleted = models.BooleanField(default=False)

# OrganizationAccessAuthorization Model
class OrganizationAccessAuthorization(models.Model):
    id = models.AutoField(primary_key=True)
    accessible_org_code = models.CharField(max_length=50, null=False)
    accessible_org_level = models.IntegerField(default=1)
    organization_code = models.ForeignKey(Organization, on_delete=models.CASCADE)
    create_at = models.DateTimeField(auto_now=True)
    create_by = models.IntegerField(default=1)
    is_deleted = models.BooleanField(default=False)

# Position Model
class Position(models.Model):
    position_code = models.CharField(max_length=50, primary_key=True, null=False)
    position_name = models.CharField(max_length=200, null=False)
    create_at = models.DateTimeField(auto_now=True)
    create_by = models.IntegerField(default=1)
    is_deleted = models.BooleanField(default=False)

# Screen Model
class Screen(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, null=False)
    create_at = models.DateTimeField(auto_now=True)
    create_by = models.IntegerField(default=1)
    is_deleted = models.BooleanField(default=False)

# Role Model
class Role(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, null=False)
    create_at = models.DateTimeField(auto_now=True)
    create_by = models.IntegerField(default=1)
    is_deleted = models.BooleanField(default=False)

# RoleScreenMgmt Model
class RoleScreenMgmt(models.Model):
    id = models.AutoField(primary_key=True)
    role_id = models.ForeignKey(Role, on_delete=models.CASCADE)
    screen_id = models.ForeignKey(Screen, on_delete=models.CASCADE)
    create_at = models.DateTimeField(auto_now=True)
    create_by = models.IntegerField(default=1)
    is_deleted = models.BooleanField(default=False)

# GroupPositionRoleMgmt Model
class GroupPositionRoleMgmt(models.Model):
    id = models.AutoField(primary_key=True)
    organization_code = models.ForeignKey(Organization, on_delete=models.CASCADE)
    position_code = models.ForeignKey(Position, on_delete=models.CASCADE)
    role_id = models.ForeignKey(Role, on_delete=models.CASCADE)
    create_at = models.DateTimeField(auto_now=True)
    create_by = models.IntegerField(default=1)
    is_deleted = models.BooleanField(default=False)

# UserOrgPositionMgmt Model
class UserOrgPositionMgmt(models.Model):
    id = models.AutoField(primary_key=True)
    user_no = models.ForeignKey(User, on_delete=models.CASCADE)
    organization_code = models.ForeignKey(Organization, on_delete=models.CASCADE)
    position_code = models.ForeignKey(Position, on_delete=models.CASCADE)
    role_type = models.IntegerField(default=1)
    create_at = models.DateTimeField(auto_now=True)
    create_by = models.IntegerField(default=1)
    is_deleted = models.BooleanField(default=False)

# Section Model
class Section(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, null=False)
    biz = models.CharField(max_length=50, null=False)
    biz_detail = models.CharField(max_length=50, null=False)
    sort_order = models.IntegerField(default=1)
    create_at = models.DateTimeField(auto_now=True)
    create_by = models.IntegerField(default=1)
    is_deleted = models.BooleanField(default=False)

# LineBiz Model
class LineBiz(models.Model):
    id = models.AutoField(primary_key=True)
    section_id = models.ForeignKey(Section, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=False)
    sort_order = models.IntegerField(default=1)
    create_at = models.DateTimeField(auto_now=True)
    create_by = models.IntegerField(default=1)
    is_deleted = models.BooleanField(default=False)

# LineAreaContractedBiz Model
class LineAreaContractedBiz(models.Model):
    id = models.AutoField(primary_key=True)
    section_id = models.ForeignKey(Section, on_delete=models.CASCADE)
    line_biz_id = models.ForeignKey(LineBiz, on_delete=models.CASCADE)
    type = models.IntegerField(default=1)
    name = models.CharField(max_length=200, null=False)
    line_len = models.DecimalField(max_digits=14, decimal_places=5)
    construction_start_date = models.DateTimeField(null=True)
    create_at = models.DateTimeField(auto_now=True)
    create_by = models.IntegerField(default=1)
    is_deleted = models.BooleanField(default=False)

# LineAreaAccessAuthorization Model
class LineAreaAccessAuthorization(models.Model):
    id = models.AutoField(primary_key=True)
    line_area_contracted_biz_id = models.ForeignKey(LineAreaContractedBiz, on_delete=models.CASCADE)
    organization_code = models.ForeignKey(Organization, on_delete=models.CASCADE)
    create_at = models.DateTimeField(auto_now=True)
    create_by = models.IntegerField(default=1)
    is_deleted = models.BooleanField(default=False)
