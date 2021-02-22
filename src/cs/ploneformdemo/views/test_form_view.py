# -*- coding: utf-8 -*-
from cs.ploneformdemo import _
from plone.app.multilingual.browser.interfaces import make_relation_root_path
from plone.app.textfield import RichText
from plone.app.z3cform.widget import AjaxSelectFieldWidget
from plone.app.z3cform.widget import RelatedItemsFieldWidget
from plone.app.z3cform.widget import SelectFieldWidget
from plone.autoform import directives
from plone.dexterity.content import Container
from plone.namedfile.field import NamedBlobFile
from plone.namedfile.field import NamedBlobImage
from plone.schema.email import Email
from plone.supermodel import model
from plone.supermodel.directives import fieldset
from plone.supermodel.directives import primary
from Products.Five.browser import BrowserView
from Products.statusmessages.interfaces import IStatusMessage
from z3c.form import button
from z3c.form import field
from z3c.form import form
from z3c.form import group
from z3c.form.browser.checkbox import CheckBoxFieldWidget
from z3c.form.browser.radio import RadioFieldWidget
from z3c.relationfield.schema import Relation
from z3c.relationfield.schema import RelationChoice
from z3c.relationfield.schema import RelationList
from zope import schema
from zope.interface import implementer
from zope.interface import Interface


class ITestFormSchema(Interface):

    # fieldset(
    #     "numberfields",
    #     label=u"Number fields",
    #     fields=("int_field", "float_field"),
    # )

    # fieldset(
    #     "datetimefields",
    #     label=u"Date and time fields",
    #     fields=("datetime_field", "date_field", "time_field", "timedelta_field"),
    # )

    # fieldset(
    #     "choicefields",
    #     label=u"Choice and Multiple Choice fields",
    #     fields=(
    #         "choice_field",
    #         "choice_field_radio",
    #         "choice_field_select",
    #         "choice_field_voc",
    #         "list_field",
    #         "list_field_checkbox",
    #         "list_field_select",
    #         "list_field_voc_unconstrained",
    #         "tuple_field",
    #         "set_field",
    #         "set_field_checkbox",
    #     ),
    # )

    # fieldset(
    #     "relationfields",
    #     label=u"Relation fields",
    #     fields=("relationchoice_field", "relationlist_field"),
    # )

    # fieldset(
    #     "filefields",
    #     label=u"File fields",
    #     fields=("file_field", "image_field"),
    # )

    # fieldset(
    #     "otherfields",
    #     label=u"Other fields",
    #     fields=(
    #         "uri_field",
    #         "sourcetext_field",
    #         "ascii_field",
    #         "bytesline_field",
    #         "asciiline_field",
    #         "pythonidentifier_field",
    #         "dottedname_field",
    #         "dict_field",
    #         "dict_field_with_choice",
    #     ),
    # )

    title = schema.TextLine(
        title=u"Primary Field (Textline)",
        description=u"This is the description or help text of the field and could be very long if required",
        required=True,
    )

    text_field = schema.Text(
        title=u"Text Field",
        description=u"This is the description or help text of the field and could be very long if required",
        required=False,
        missing_value=u"",
    )

    textline_field = schema.TextLine(
        title=u"Textline field",
        description=u"This is the description or help text of the field and could be very long if required",
        required=False,
    )

    bool_field = schema.Bool(
        title=u"Boolean field",
        description=u"This is the description or help text of the field and could be very long if required",
        required=False,
    )

    choice_field = schema.Choice(
        title=u"Choice field",
        description=u"This is the description or help text of the field and could be very long if required",
        values=[u"One", u"Two", u"Three"],
        required=True,
    )

    directives.widget(choice_field_radio=RadioFieldWidget)
    choice_field_radio = schema.Choice(
        title=u"Choice field with radio boxes",
        description=u"This is the description or help text of the field and could be very long if required",
        values=[u"One", u"Two", u"Three"],
        required=True,
    )

    choice_field_voc = schema.Choice(
        title=u"Choicefield with values from named vocabulary",
        description=u"This is the description or help text of the field and could be very long if required",
        vocabulary="plone.app.vocabularies.PortalTypes",
        required=False,
    )

    directives.widget(choice_field_select=SelectFieldWidget)
    choice_field_select = schema.Choice(
        title=u"Choicefield with select2 widget",
        description=u"This is the description or help text of the field and could be very long if required",
        vocabulary="plone.app.vocabularies.PortalTypes",
        required=False,
    )

    list_field = schema.List(
        title=u"List field",
        description=u"This is the description or help text of the field and could be very long if required",
        value_type=schema.Choice(
            values=[u"Beginner", u"Advanced", u"Professional"],
        ),
        required=False,
        missing_value=[],
    )

    directives.widget(list_field_checkbox=CheckBoxFieldWidget)
    list_field_checkbox = schema.List(
        title=u"List field with checkboxes",
        description=u"This is the description or help text of the field and could be very long if required",
        value_type=schema.Choice(
            values=[u"Beginner", u"Advanced", u"Professional"],
        ),
        required=False,
        missing_value=[],
    )

    directives.widget(list_field_select=SelectFieldWidget)
    list_field_select = schema.List(
        title=u"List field with select widget",
        description=u"This is the description or help text of the field and could be very long if required",
        value_type=schema.Choice(
            values=[u"Beginner", u"Advanced", u"Professional"],
        ),
        required=False,
        missing_value=[],
    )

    list_field_voc_unconstrained = schema.List(
        title=u"List field with values from vocabulary but not constrained to them.",
        description=u"This is the description or help text of the field and could be very long if required",
        value_type=schema.TextLine(),
        required=False,
        missing_value=[],
    )
    directives.widget(
        "list_field_voc_unconstrained",
        AjaxSelectFieldWidget,
        vocabulary="plone.app.vocabularies.Users",
    )

    tuple_field = schema.Tuple(
        title=u"Tuple field",
        description=u"This is the description or help text of the field and could be very long if required",
        value_type=schema.Choice(
            values=[u"Beginner", u"Advanced", u"Professional"],
        ),
        required=False,
        missing_value=(),
    )

    set_field = schema.Set(
        title=u"Set field",
        description=u"This is the description or help text of the field and could be very long if required",
        value_type=schema.Choice(
            values=[u"Beginner", u"Advanced", u"Professional"],
        ),
        required=False,
        missing_value={},
    )

    directives.widget(set_field_checkbox=CheckBoxFieldWidget)
    set_field_checkbox = schema.Set(
        title=u"Set field with checkboxes",
        description=u"This is the description or help text of the field and could be very long if required",
        value_type=schema.Choice(
            values=[u"Beginner", u"Advanced", u"Professional"],
        ),
        required=False,
        missing_value={},
    )

    # File fields
    image_field = NamedBlobImage(
        title=u"Image field",
        description=u"This is the description or help text of the field and could be very long if required",
        required=False,
    )

    file_field = NamedBlobFile(
        title=u"File field",
        description=u"This is the description or help text of the field and could be very long if required",
        required=False,
    )

    # Date and Time fields
    datetime_field = schema.Datetime(
        title=u"Datetime field",
        description=u"This is the description or help text of the field and could be very long if required",
        required=False,
    )

    date_field = schema.Date(
        title=u"Date field",
        description=u"This is the description or help text of the field and could be very long if required",
        required=False,
    )

    time_field = schema.Time(
        title=u"Time field",
        description=u"This is the description or help text of the field and could be very long if required",
        required=False,
    )

    timedelta_field = schema.Timedelta(
        title=u"Timedelta field",
        description=u"This is the description or help text of the field and could be very long if required",
        required=False,
    )

    # Relation Fields
    relationchoice_field = RelationChoice(
        title=u"Relationchoice field",
        description=u"This is the description or help text of the field and could be very long if required",
        vocabulary="plone.app.vocabularies.Catalog",
        required=False,
    )
    directives.widget(
        "relationchoice_field",
        RelatedItemsFieldWidget,
        pattern_options={
            "selectableTypes": ["Document"],
            "basePath": make_relation_root_path,
        },
    )

    relationlist_field = RelationList(
        title=u"Relationlist Field",
        description=u"This is the description or help text of the field and could be very long if required",
        default=[],
        value_type=RelationChoice(vocabulary="plone.app.vocabularies.Catalog"),
        required=False,
        missing_value=[],
    )
    directives.widget(
        "relationlist_field",
        RelatedItemsFieldWidget,
        vocabulary="plone.app.vocabularies.Catalog",
        pattern_options={
            "selectableTypes": ["Document"],
            "basePath": make_relation_root_path,
        },
    )

    # Number fields
    int_field = schema.Int(
        title=u"Integer Field (e.g. 12)",
        description=u"This is the description or help text of the field and could be very long if required",
        required=False,
    )

    float_field = schema.Float(
        title=u"Float field (e.g. 12.2)",
        description=u"This is the description or help text of the field and could be very long if required",
        required=False,
    )

    # Text fields
    email_field = Email(
        title=u"Email field",
        description=u"This is the description or help text of the field and could be very long if required",
        required=False,
    )

    uri_field = schema.URI(
        title=u"URI field",
        description=u"This is the description or help text of the field and could be very long if required",
        required=False,
    )

    richtext_field = RichText(
        title=u"RichText field",
        description=u"This is the description or help text of the field and could be very long if required",
        max_length=2000,
        required=False,
    )

    sourcetext_field = schema.SourceText(
        title=u"SourceText field",
        description=u"This is the description or help text of the field and could be very long if required",
        required=False,
    )

    ascii_field = schema.ASCII(
        title=u"ASCII field",
        description=u"This is the description or help text of the field and could be very long if required",
        required=False,
    )

    bytesline_field = schema.BytesLine(
        title=u"BytesLine field",
        description=u"This is the description or help text of the field and could be very long if required",
        required=False,
    )

    asciiline_field = schema.ASCIILine(
        title=u"ASCIILine field",
        description=u"This is the description or help text of the field and could be very long if required",
        required=False,
    )

    pythonidentifier_field = schema.PythonIdentifier(
        title=u"PythonIdentifier field",
        description=u"This is the description or help text of the field and could be very long if required",
        required=False,
    )

    dottedname_field = schema.DottedName(
        title=u"DottedName field",
        description=u"This is the description or help text of the field and could be very long if required",
        required=False,
    )

    dict_field = schema.Dict(
        title=u"Dict field",
        description=u"This is the description or help text of the field and could be very long if required",
        required=False,
        key_type=schema.TextLine(
            title=u"Key",
            required=False,
        ),
        value_type=schema.TextLine(
            title=u"Value",
            required=False,
        ),
    )

    dict_field_with_choice = schema.Dict(
        title=u"Dict field with key and value as choice",
        description=u"This is the description or help text of the field and could be very long if required",
        required=False,
        key_type=schema.Choice(
            title=u"Key",
            values=[u"One", u"Two", u"Three"],
            required=False,
        ),
        value_type=schema.Set(
            title=u"Value",
            value_type=schema.Choice(
                values=[u"Beginner", u"Advanced", u"Professional"],
            ),
            required=False,
            missing_value={},
        ),
    )


class NumberGroup(group.Group):
    label = _(u"Number fields")
    fields = field.Fields(ITestFormSchema).select("int_field", "float_field")


class DateTimeGroup(group.Group):
    label = _(u"DateTime fields")
    fields = field.Fields(ITestFormSchema).select(
        "datetime_field", "date_field", "time_field", "timedelta_field"
    )


class ChoiceGroup(group.Group):
    label = _(u"Choice fields")
    fields = field.Fields(ITestFormSchema).select(
        "choice_field",
        "choice_field_radio",
        "choice_field_select",
        "choice_field_voc",
        "list_field",
        "list_field_checkbox",
        "list_field_select",
        "list_field_voc_unconstrained",
        "tuple_field",
        "set_field",
        "set_field_checkbox",
    )


class RelationGroup(group.Group):
    label = _(u"Relation fields")
    fields = field.Fields(ITestFormSchema).select(
        "relationchoice_field", "relationlist_field"
    )


class FileGroup(group.Group):
    label = _(u"File fields")
    fields = field.Fields(ITestFormSchema).select("file_field", "image_field")


class OtherGroup(group.Group):
    label = _(u"Other fields")

    fields = field.Fields(ITestFormSchema).select(
        "uri_field",
        "sourcetext_field",
        "ascii_field",
        "bytesline_field",
        "asciiline_field",
        "pythonidentifier_field",
        "dottedname_field",
        "dict_field",
        "dict_field_with_choice",
    )


class TestFormView(form.Form):
    ignoreContext = True
    method = "post"
    fields = field.Fields(ITestFormSchema)

    def updateWidgets(self, *args, **kwargs):
        super(TestFormView, self).updateWidgets(*args, **kwargs)
        self.widgets["int_field"].placeholder = "This is the placeholder value for this field"
        self.widgets["title"].placeholder = "This is the placeholder value for this field"
        self.widgets["text_field"].placeholder = "This is the placeholder value for this field"

    @button.buttonAndHandler(_(u"Send"))
    def handleApply(self, action):
        data, errors = self.extractData()

        if errors:
            error_message = _(
                u"You must complete this form correctly, especially those fields marked as required."
            )
            IStatusMessage(self.request).addStatusMessage(error_message, type="error")
            return

        ret = self.send_data(data)
        if not ret:
            error_message = _(
                u"There was an error sending the message, try again please."
            )
            IStatusMessage(self.request).addStatusMessage(error_message, type="error")

        else:
            url = "%s/%s" % (self.context.absolute_url(), "test-form-view")
            return self.request.response.redirect(url)


class TestForm2View(group.GroupForm, form.Form):
    ignoreContext = True
    method = "post"

    groups = (
        NumberGroup,
        DateTimeGroup,
        ChoiceGroup,
        RelationGroup,
        FileGroup,
        OtherGroup,
    )

    @button.buttonAndHandler(_(u"Send"))
    def handleApply(self, action):
        data, errors = self.extractData()

        if errors:
            error_message = _(
                u"You must complete this form correctly, especially those fields marked as required."
            )
            IStatusMessage(self.request).addStatusMessage(error_message, type="error")
            return

        ret = self.send_data(data)
        if not ret:
            error_message = _(
                u"There was an error sending the message, try again please."
            )
            IStatusMessage(self.request).addStatusMessage(error_message, type="error")

        else:
            url = "%s/%s" % (self.context.absolute_url(), "test-form-view")
            return self.request.response.redirect(url)
