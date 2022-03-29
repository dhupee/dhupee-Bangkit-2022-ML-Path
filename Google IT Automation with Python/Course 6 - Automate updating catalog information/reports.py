from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph, Spacer, Table, Image
from reportlab.lib.styles import getSampleStyleSheet


def generate_report(attachment, title, paragraph):
    styles = getSampleStyleSheet()
    report = SimpleDocTemplate(filename)
    report_title = Paragraph(title, styles["h1"])
    report_paragraph = Paragraph(paragraph, styles["BodyText"])
    empty_line = Spacer(1, 20)
    report.build([report_title, report_paragraph])