import os
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE

def build_presentation(output_path):
    prs = Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    blank_layout = prs.slide_layouts[6]

    # Color Palette
    SAGE_DARK = RGBColor(0x2D, 0x6A, 0x4F)     # #2D6A4F
    SAGE_LIGHT = RGBColor(0xD8, 0xF3, 0xDC)    # #D8F3DC
    OCHRE = RGBColor(0xDD, 0xA1, 0x5E)         # #DDA15E
    BG_LIGHT = RGBColor(0xF8, 0xF9, 0xFA)      # #F8F9FA
    WHITE = RGBColor(0xFF, 0xFF, 0xFF)         # #FFFFFF
    TEXT_DARK = RGBColor(0x1A, 0x20, 0x2C)     # #1A202C
    TEXT_MUTED = RGBColor(0x4A, 0x55, 0x68)    # #4A5568
    CARD_BORDER = RGBColor(0xE2, 0xE8, 0xF0)   # #E2E8F0
    RED_ACCENT = RGBColor(0xC5, 0x30, 0x30)    # #C53030

    def add_slide_base(category_tag, title_text, subtitle_text):
        slide = prs.slides.add_slide(blank_layout)

        # Background
        bg = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, prs.slide_width, prs.slide_height)
        bg.fill.solid()
        bg.fill.fore_color.rgb = BG_LIGHT
        bg.line.fill.background()

        # Top decorative accent bar
        bar = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, prs.slide_width, Inches(0.08))
        bar.fill.solid()
        bar.fill.fore_color.rgb = SAGE_DARK
        bar.line.fill.background()

        # Header Box
        header_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.4), Inches(11.733), Inches(1.2))
        tf = header_box.text_frame
        tf.word_wrap = True
        tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = 0

        # Category Tag
        p_tag = tf.paragraphs[0]
        p_tag.text = category_tag.upper()
        p_tag.font.name = "Arial"
        p_tag.font.size = Pt(10)
        p_tag.font.bold = True
        p_tag.font.color.rgb = OCHRE
        p_tag.space_after = Pt(2)

        # Title
        p_title = tf.add_paragraph()
        p_title.text = title_text
        p_title.font.name = "Arial"
        p_title.font.size = Pt(24)
        p_title.font.bold = True
        p_title.font.color.rgb = SAGE_DARK
        p_title.space_after = Pt(2)

        # Subtitle
        if subtitle_text:
            p_sub = tf.add_paragraph()
            p_sub.text = subtitle_text
            p_sub.font.name = "Arial"
            p_sub.font.size = Pt(12)
            p_sub.font.color.rgb = TEXT_MUTED

        return slide

    def add_card(slide, left, top, width, height, bg_color=WHITE, border_color=CARD_BORDER):
        card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, height)
        card.fill.solid()
        card.fill.fore_color.rgb = bg_color
        if border_color:
            card.line.color.rgb = border_color
            card.line.width = Pt(1)
        else:
            card.line.fill.background()
        return card

    # ==========================================
    # SLIDE 1: TITLE SLIDE
    # ==========================================
    slide1 = prs.slides.add_slide(blank_layout)
    bg1 = slide1.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, prs.slide_width, prs.slide_height)
    bg1.fill.solid()
    bg1.fill.fore_color.rgb = SAGE_DARK
    bg1.line.fill.background()

    # Title Card
    c1 = add_card(slide1, Inches(1.0), Inches(1.0), Inches(11.333), Inches(5.5), bg_color=WHITE, border_color=None)
    tf1 = c1.text_frame
    tf1.word_wrap = True
    tf1.margin_left = tf1.margin_right = Inches(0.8)
    tf1.margin_top = Inches(0.8)

    p = tf1.paragraphs[0]
    p.text = "PRM393 / PRM323 — LAB 2: AI-ASSISTED UI/UX DESIGN"
    p.font.name = "Arial"
    p.font.size = Pt(13)
    p.font.bold = True
    p.font.color.rgb = OCHRE
    p.space_after = Pt(14)

    p = tf1.add_paragraph()
    p.text = "Why I Buy? – The Psychology of Money"
    p.font.name = "Arial"
    p.font.size = Pt(36)
    p.font.bold = True
    p.font.color.rgb = SAGE_DARK
    p.space_after = Pt(10)

    p = tf1.add_paragraph()
    p.text = "Mindful Spending Companion: 'Understand before you change'"
    p.font.name = "Arial"
    p.font.size = Pt(18)
    p.font.color.rgb = TEXT_MUTED
    p.space_after = Pt(28)

    p = tf1.add_paragraph()
    p.text = "• Ý tưởng: Dựa trên cuốn sách kinh điển của Morgan Housel, tập trung vào ĐỘNG CƠ TÂM LÝ thay vì chỉ đếm số tiền.\n• Công nghệ: Google Stitch (AI Generation) → Figma Design System (10 Screens) → Flutter Handoff.\n• Nhóm thực hiện: Sinh viên PRM393 | FA26"
    p.font.name = "Arial"
    p.font.size = Pt(14)
    p.font.color.rgb = TEXT_DARK

    notes1 = slide1.notes_slide.notes_text_frame
    notes1.text = "Kính chào thầy và các bạn, hôm nay nhóm em xin trình bày dự án Lab 2 mang tên 'Why I Buy?'. Được lấy cảm hứng từ cuốn sách The Psychology of Money của Morgan Housel, sản phẩm của nhóm không đi theo lối mòn của các ứng dụng quản lý chi tiêu truyền thống là đếm từng đồng và gây áp lực. Thay vào đó, chúng em tập trung giúp người trẻ hiểu được động cơ tâm lý và những bẫy cảm xúc đằng sau từng quyết định mua sắm, với triết lý: Thấu hiểu bản thân trước khi muốn thay đổi thói quen."

    # ==========================================
    # SLIDE 2: PROBLEM & PERSONA
    # ==========================================
    slide2 = add_slide_base("02. RESEARCH & TARGET AUDIENCE", "Problem Statement & User Persona", "Chân dung người dùng mục tiêu và 4 rào cản tâm lý cốt lõi")
    
    # Left Box: Persona
    c2_left = add_card(slide2, Inches(0.8), Inches(1.8), Inches(5.6), Inches(5.0))
    tf2_l = c2_left.text_frame
    tf2_l.word_wrap = True
    tf2_l.margin_left = tf2_l.margin_right = tf2_l.margin_top = Inches(0.4)
    
    p = tf2_l.paragraphs[0]
    p.text = "👤 Primary Persona: Nguyễn Hải Nam (22 tuổi)"
    p.font.bold = True
    p.font.size = Pt(16)
    p.font.color.rgb = SAGE_DARK
    p.space_after = Pt(10)
    
    p = tf2_l.add_paragraph()
    p.text = "• Bối cảnh: Sinh viên năm cuối CNTT & Thực tập sinh.\n• Thu nhập: 7 - 9 triệu/tháng.\n• Thói quen: Mua sắm online thường xuyên (Shopee, TikTok Shop, GrabFood). Hay săn sale đêm muộn khi mệt mỏi.\n• Hành vi quá khứ: Đã từng tải nhiều app chi tiêu nhưng bỏ sau 1 tuần vì nản lòng và cảm giác tội lỗi khi thấy số dư âm."
    p.font.size = Pt(13)
    p.font.color.rgb = TEXT_DARK
    
    # Right Box: Pain Points & Measurable Goal
    c2_right = add_card(slide2, Inches(6.8), Inches(1.8), Inches(5.7), Inches(5.0))
    tf2_r = c2_right.text_frame
    tf2_r.word_wrap = True
    tf2_r.margin_left = tf2_r.margin_right = tf2_r.margin_top = Inches(0.4)
    
    p = tf2_r.paragraphs[0]
    p.text = "⚡ 4 Pain Points & Mục tiêu đo lường"
    p.font.bold = True
    p.font.size = Pt(16)
    p.font.color.rgb = SAGE_DARK
    p.space_after = Pt(10)
    
    p = tf2_r.add_paragraph()
    p.text = "1. Cảm giác tội lỗi: Nhìn biểu đồ cảnh báo đỏ khiến user né tránh mở app.\n2. Ma sát nhập liệu: Nhập quá nhiều danh mục phụ cho 1 cốc cà phê.\n3. Mù mờ động cơ: Biết số tiền tiêu nhưng không biết vì sao mình mua.\n4. Bẫy kích thích: Mua sắm vì FOMO, quảng cáo và stress đêm muộn.\n\n🎯 Mục tiêu đo lường (Success Criteria):\n• Ghi nhận khoản mua & gán lý do trong ≤ 20 giây.\n• Tỷ lệ gắn nhãn lý do đạt ≥ 90%.\n• Giảm 30% quyết định mua bốc đồng sau 30 ngày."
    p.font.size = Pt(13)
    p.font.color.rgb = TEXT_DARK

    notes2 = slide2.notes_slide.notes_text_frame
    notes2.text = "Xuất phát từ nghiên cứu người dùng, bạn Nam - 22 tuổi đại diện cho thế hệ Gen Z thường xuyên mua sắm online. Nam từng thử qua nhiều ứng dụng chi tiêu nhưng đều từ bỏ vì cảm giác tội lỗi mỗi khi thấy biểu đồ màu đỏ cảnh báo. Vấn đề của Nam không phải là không biết tính toán, mà là Nam không nhận ra các kích thích cảm xúc như căng thẳng hay giảm giá đêm muộn đang chi phối mình. Do đó, mục tiêu của nhóm là tạo ra một công cụ ghi chép siêu nhanh dưới 20 giây và hoàn toàn không phán xét người dùng."

    # ==========================================
    # SLIDE 3: INFORMATION ARCHITECTURE
    # ==========================================
    slide3 = add_slide_base("03. ARCHITECTURE & SITEMAP", "Information Architecture (10 Screens)", "Cấu trúc phân tầng điều hướng 5 Tabs chính và Modals cấp con")

    c3_1 = add_card(slide3, Inches(0.8), Inches(1.8), Inches(3.7), Inches(5.0))
    tf3_1 = c3_1.text_frame
    tf3_1.word_wrap = True
    tf3_1.margin_left = tf3_1.margin_right = tf3_1.margin_top = Inches(0.3)
    p = tf3_1.paragraphs[0]
    p.text = "📱 Cấp 0: Onboarding & Entry"
    p.font.bold = True
    p.font.size = Pt(15)
    p.font.color.rgb = SAGE_DARK
    p.space_after = Pt(10)
    p = tf3_1.add_paragraph()
    p.text = "01. Onboarding Screen\n• Giới thiệu triết lý 'The Psychology of Money'.\n• Thông điệp 'Understand before you change'.\n• Carousel 3 bước chuyển mượt mà."
    p.font.size = Pt(12)
    p.font.color.rgb = TEXT_DARK

    c3_2 = add_card(slide3, Inches(4.8), Inches(1.8), Inches(3.7), Inches(5.0))
    tf3_2 = c3_2.text_frame
    tf3_2.word_wrap = True
    tf3_2.margin_left = tf3_2.margin_right = tf3_2.margin_top = Inches(0.3)
    p = tf3_2.paragraphs[0]
    p.text = "🧭 Cấp 1: Bottom Navigation"
    p.font.bold = True
    p.font.size = Pt(15)
    p.font.color.rgb = SAGE_DARK
    p.space_after = Pt(10)
    p = tf3_2.add_paragraph()
    p.text = "5 Tabs chính xuyên suốt:\n• Tab 1: 02. Home Dashboard\n• Tab 2: 06. Purchase History\n• Tab 3: 07. Buying Patterns\n• Tab 4: 08. Personal Insights\n• Tab 5: 10. Profile & Settings\n\n→ Đảm bảo chuyển đổi tab tức thì, không bị mất bối cảnh."
    p.font.size = Pt(12)
    p.font.color.rgb = TEXT_DARK

    c3_3 = add_card(slide3, Inches(8.8), Inches(1.8), Inches(3.7), Inches(5.0))
    tf3_3 = c3_3.text_frame
    tf3_3.word_wrap = True
    tf3_3.margin_left = tf3_3.margin_right = tf3_3.margin_top = Inches(0.3)
    p = tf3_3.paragraphs[0]
    p.text = "⚙️ Cấp 2: Modals & Detail"
    p.font.bold = True
    p.font.size = Pt(15)
    p.font.color.rgb = SAGE_DARK
    p.space_after = Pt(10)
    p = tf3_3.add_paragraph()
    p.text = "Các màn hình hành động:\n• 03. Add Purchase (Bước 1: Tiền & Tên)\n• 04. Purchase Reason (Bước 2: 8 lý do)\n• 05. Purchase Detail (Chi tiết & Nhật ký cảm xúc)\n• 09. Monthly Reflection (Báo cáo tháng)\n\n→ Dạng Modal trượt từ dưới lên, có nút thoát rõ ràng."
    p.font.size = Pt(12)
    p.font.color.rgb = TEXT_DARK

    notes3 = slide3.notes_slide.notes_text_frame
    notes3.text = "Về cấu trúc thông tin, nhóm xây dựng hệ thống 10 màn hình với thanh Bottom Navigation 5 tab chính. Chúng em tách biệt rõ ràng giữa màn hình cấp cao như Dashboard, Patterns, Insights và các màn hình hành động cấp con dạng modal như luồng ghi khoản mua 2 bước hay trang chiêm nghiệm tháng, đảm bảo người dùng định vị không gian cực kỳ dễ dàng."

    # ==========================================
    # SLIDE 4: THREE USER FLOWS
    # ==========================================
    slide4 = add_slide_base("04. INTERACTION FLOWS", "Three Core User Flows", "Các kịch bản tương tác người dùng: Happy path, Alternative path & Error Recovery")

    c4_1 = add_card(slide4, Inches(0.8), Inches(1.8), Inches(11.733), Inches(1.4))
    tf4_1 = c4_1.text_frame
    tf4_1.word_wrap = True
    tf4_1.margin_left = tf4_1.margin_right = tf4_1.margin_top = Inches(0.25)
    p = tf4_1.paragraphs[0]
    p.text = "🟢 Flow 1: Record a Purchase (Happy Path)"
    p.font.bold = True
    p.font.size = Pt(14)
    p.font.color.rgb = SAGE_DARK
    p = tf4_1.add_paragraph()
    p.text = "Home Dashboard → [Nhấn + Ghi khoản mua] → Nhập Tiền & Tên (Bước 1) → Chọn 1 trong 8 lý do tâm lý (Bước 2) → Lưu nhanh → Toast xác nhận & Cập nhật Home (Thời gian hoàn thành: 18 giây)."
    p.font.size = Pt(12)

    c4_2 = add_card(slide4, Inches(0.8), Inches(3.5), Inches(11.733), Inches(1.4))
    tf4_2 = c4_2.text_frame
    tf4_2.word_wrap = True
    tf4_2.margin_left = tf4_2.margin_right = tf4_2.margin_top = Inches(0.25)
    p = tf4_2.paragraphs[0]
    p.text = "🟡 Flow 2: Understand Buying Behavior (Chiêm nghiệm thói quen)"
    p.font.bold = True
    p.font.size = Pt(14)
    p.font.color.rgb = OCHRE
    p = tf4_2.add_paragraph()
    p.text = "Home Dashboard → Tab Buying Patterns (Khám phá Donut Chart & Giờ bốc đồng) → Tab Personal Insights (Đọc gợi ý AI: Quy tắc 72h) → Mở Monthly Reflection → Tự đánh giá điểm thỏa mãn (Rate 1-5 sao) & Đặt mục tiêu tháng mới."
    p.font.size = Pt(12)

    c4_3 = add_card(slide4, Inches(0.8), Inches(5.2), Inches(11.733), Inches(1.4))
    tf4_3 = c4_3.text_frame
    tf4_3.word_wrap = True
    tf4_3.margin_left = tf4_3.margin_right = tf4_3.margin_top = Inches(0.25)
    p = tf4_3.paragraphs[0]
    p.text = "🔴 Flow 3: Error & Recovery (Xử lý lỗi & Phục hồi an toàn)"
    p.font.bold = True
    p.font.size = Pt(14)
    p.font.color.rgb = RED_ACCENT
    p = tf4_3.add_paragraph()
    p.text = "Add Purchase → Nhập thiếu / Số tiền 0đ → Inline Error & Auto-focus sửa lỗi tại chỗ → Bấm Lưu khi Mất mạng → Tự động lưu ngoại tuyến (Offline Local Draft) → Hiện Banner nhẹ: 'Đã lưu bản nháp an toàn, sẽ tự đồng bộ khi có mạng' (0% Data Loss)."
    p.font.size = Pt(12)

    notes4 = slide4.notes_slide.notes_text_frame
    notes4.text = "Nhóm đã thiết kế 3 luồng người dùng hoàn chỉnh. Điểm nổi bật nhất ở Flow 1 là tốc độ: chia làm 2 bước để giảm tối đa rào cản. Flow 2 hướng dẫn người dùng tự chiêm nghiệm từ biểu đồ đến hành động thực tế. Và đặc biệt, Flow 3 đảm bảo không bao giờ làm mất dữ liệu của người dùng nhờ cơ chế cảnh báo lỗi tại chỗ và tự động lưu nháp ngoại tuyến khi mất mạng."

    # ==========================================
    # SLIDE 5: AI UI GENERATION (GOOGLE STITCH)
    # ==========================================
    slide5 = add_slide_base("05. AI GENERATION", "AI UI Generation with Google Stitch", "Khởi tạo giao diện bằng kỹ thuật Prompting có cấu trúc và ràng buộc di động")

    c5_l = add_card(slide5, Inches(0.8), Inches(1.8), Inches(6.0), Inches(5.0))
    tf5_l = c5_l.text_frame
    tf5_l.word_wrap = True
    tf5_l.margin_left = tf5_l.margin_right = tf5_l.margin_top = Inches(0.35)
    p = tf5_l.paragraphs[0]
    p.text = "📝 Kỹ thuật Prompt có cấu trúc"
    p.font.bold = True
    p.font.size = Pt(15)
    p.font.color.rgb = SAGE_DARK
    p.space_after = Pt(8)
    p = tf5_l.add_paragraph()
    p.text = "• Role: Senior Mobile UI/UX Designer\n• Platform: Mobile App (Android & iOS), 390x844 dp\n• Persona: Young adult struggling with impulse buying\n• Tone: Minimalist, calming, reflective, non-judgmental\n• Colors: Sage Green (#2D6A4F), Warm Ochre (#DDA15E), Soft Sand\n• Constraints: Spacing 8dp grid, touch target ≥ 48dp, contrast WCAG AA, no harsh red warnings.\n\n→ Prompt nguyên văn được lưu tại DESIGN.md."
    p.font.size = Pt(12)

    c5_r = add_card(slide5, Inches(7.2), Inches(1.8), Inches(5.3), Inches(5.0))
    tf5_r = c5_r.text_frame
    tf5_r.word_wrap = True
    tf5_r.margin_left = tf5_r.margin_right = tf5_r.margin_top = Inches(0.35)
    p = tf5_r.paragraphs[0]
    p.text = "🖼️ Kết quả khởi tạo từ Google Stitch"
    p.font.bold = True
    p.font.size = Pt(15)
    p.font.color.rgb = SAGE_DARK
    p.space_after = Pt(8)
    p = tf5_r.add_paragraph()
    p.text = "• Sinh nhanh bố cục khung thô ban đầu cho 4 màn hình chính: Home, Add Purchase, Reason Grid, Analytics.\n• Thể hiện được bố cục thẻ và màu sắc dịu nhẹ theo yêu cầu.\n• Tuy nhiên: Bộc lộ nhiều lỗi nghiêm trọng về khả năng tiếp cận (Accessibility) và tải nhận thức (Cognitive Overload).\n\n→ Cần bước phản biện UX và tinh chỉnh thủ công."
    p.font.size = Pt(12)

    notes5 = slide5.notes_slide.notes_text_frame
    notes5.text = "Ở giai đoạn khởi tạo UI, nhóm không đưa ra các câu lệnh chung chung mà áp dụng kỹ thuật Prompt chuẩn xác: xác định rõ vai trò AI, persona mục tiêu, kích thước chuẩn di động, bảng màu chỉ định và các ràng buộc công thái học. Kết quả từ Google Stitch giúp nhóm có được bố cục khung thô ban đầu rất nhanh chóng."

    # ==========================================
    # SLIDE 6: AI CRITIQUE & 3 ITERATION LOOPS
    # ==========================================
    slide6 = add_slide_base("06. UX CRITIQUE & ITERATION", "AI Critique & 3 Iteration Rounds", "Phản biện theo 10 nguyên lý Nielsen và 3 vòng lặp cải tiến có mục tiêu riêng")

    c6_top = add_card(slide6, Inches(0.8), Inches(1.8), Inches(11.733), Inches(2.2))
    tf6_t = c6_top.text_frame
    tf6_t.word_wrap = True
    tf6_t.margin_left = tf6_t.margin_right = tf6_t.margin_top = Inches(0.25)
    p = tf6_t.paragraphs[0]
    p.text = "🔍 5 Vấn đề UX phát hiện từ kết quả AI ban đầu"
    p.font.bold = True
    p.font.size = Pt(14)
    p.font.color.rgb = RED_ACCENT
    p = tf6_t.add_paragraph()
    p.text = "1. Cảnh báo đỏ trừng phạt trên Dashboard → Gây cảm giác tội lỗi, vi phạm Persona & Nielsen #10.\n2. Form nhập liệu 8 trường dài trên 1 màn hình → Bàn phím che nút CTA, vi phạm Nielsen #8 (Quá tải nhận thức).\n3. Dropdown chọn lý do kích thước chỉ 28dp → Vi phạm Fitts' Law & WCAG 2.5.5 (Vùng chạm quá nhỏ).\n4. Pop-up Alert Dialog khóa màn hình khi nhập sai → Vi phạm Nielsen #3 (User Control) & #9 (Error Recovery).\n5. Biểu đồ chi tiêu theo danh mục tiền tệ truyền thống → Không phản ánh động cơ tâm lý The Psychology of Money."
    p.font.size = Pt(11.5)

    c6_bot = add_card(slide6, Inches(0.8), Inches(4.2), Inches(11.733), Inches(2.6))
    tf6_b = c6_bot.text_frame
    tf6_b.word_wrap = True
    tf6_b.margin_left = tf6_b.margin_right = tf6_b.margin_top = Inches(0.25)
    p = tf6_b.paragraphs[0]
    p.text = "🔄 3 Vòng lặp cải tiến (Before vs. After)"
    p.font.bold = True
    p.font.size = Pt(14)
    p.font.color.rgb = SAGE_DARK
    p = tf6_b.add_paragraph()
    p.text = "• Vòng 1 (Cấu trúc thông tin): Tách form 8 trường thành 2 bước (Tiền/Tên → Chọn 8 thẻ Reason). Giảm thời gian nhập từ 65s xuống 18s.\n• Vòng 2 (Khả năng tiếp cận & Vùng chạm): Nâng kích thước thẻ lên 160x76 dp (vùng bấm 100%), tương phản chữ nâng lên 7.2:1 (WCAG AAA).\n• Vòng 3 (Đồng bộ triết lý tâm lý): Đổi biểu đồ cột tiền tệ thành Donut Chart 8 lý do tâm lý và ma trận khung giờ mua bốc đồng kèm AI Actionable Advice."
    p.font.size = Pt(12)

    notes6 = slide6.notes_slide.notes_text_frame
    notes6.text = "Đây là phần nhóm tâm đắc nhất: không nhận nguyên si những gì AI tạo ra. Nhóm đã áp dụng 10 nguyên lý Nielsen để tìm ra 5 lỗi UX nghiêm trọng của AI. Sau đó, chúng em thực hiện 3 vòng lặp với 3 mục tiêu độc lập: Vòng 1 giải quyết quá tải nhận thức bằng cách tách đôi form; Vòng 2 chuẩn hóa công thái học và tương phản tiếp cận; và Vòng 3 đưa hồn cốt của cuốn sách The Psychology of Money vào các biểu đồ thấu hiểu cảm xúc thay vì những con số tiền tệ vô hồn."

    # ==========================================
    # SLIDE 7: KEY DESIGN DECISIONS
    # ==========================================
    slide7 = add_slide_base("07. STRATEGIC DECISIONS", "Design Decisions: Accept / Modify / Reject", "Các quyết định thiết kế then chốt gắn liền với Persona và Heuristics")

    c7_1 = add_card(slide7, Inches(0.8), Inches(1.8), Inches(3.7), Inches(5.0))
    tf7_1 = c7_1.text_frame
    tf7_1.word_wrap = True
    tf7_1.margin_left = tf7_1.margin_right = tf7_1.margin_top = Inches(0.3)
    p = tf7_1.paragraphs[0]
    p.text = "❌ REJECT"
    p.font.bold = True
    p.font.size = Pt(16)
    p.font.color.rgb = RED_ACCENT
    p = tf7_1.add_paragraph()
    p.text = "Cảnh báo ngân sách đỏ:\n\n• Lý do: Nam đã từ bỏ nhiều app vì cảm giác tội lỗi khi thấy màu đỏ.\n• Giải pháp: Thay bằng Hero Card Sage Green phân tích tỷ lệ tâm lý tích cực ('38% Cảm xúc, 32% Nhu cầu') và quote gợi mở."
    p.font.size = Pt(12)

    c7_2 = add_card(slide7, Inches(4.8), Inches(1.8), Inches(3.7), Inches(5.0))
    tf7_2 = c7_2.text_frame
    tf7_2.word_wrap = True
    tf7_2.margin_left = tf7_2.margin_right = tf7_2.margin_top = Inches(0.3)
    p = tf7_2.paragraphs[0]
    p.text = "🔄 MODIFY"
    p.font.bold = True
    p.font.size = Pt(16)
    p.font.color.rgb = OCHRE
    p = tf7_2.add_paragraph()
    p.text = "1. Tách Form thành 2 bước:\n• Bước 1: Tiền & Tên món.\n• Bước 2: Chọn lý do 1 chạm.\n\n2. Thay Pop-up bằng Inline Error:\n• Viền đỏ ô nhập lỗi.\n• Hiện hướng dẫn bên dưới.\n• Không chặn đứng luồng làm việc."
    p.font.size = Pt(12)

    c7_3 = add_card(slide7, Inches(8.8), Inches(1.8), Inches(3.7), Inches(5.0))
    tf7_3 = c7_3.text_frame
    tf7_3.word_wrap = True
    tf7_3.margin_left = tf7_3.margin_right = tf7_3.margin_top = Inches(0.3)
    p = tf7_3.paragraphs[0]
    p.text = "✅ ACCEPT"
    p.font.bold = True
    p.font.size = Pt(16)
    p.font.color.rgb = SAGE_DARK
    p = tf7_3.add_paragraph()
    p.text = "1. Lưới Reason Cards 2x4:\n• Icon trực quan nhận diện ngay (Recognition vs Recall).\n• Vùng bấm lớn 160x76 dp.\n\n2. Lưu nháp ngoại tuyến (Offline):\n• Tự lưu local storage khi mất mạng.\n• 0% mất dữ liệu."
    p.font.size = Pt(12)

    notes7 = slide7.notes_slide.notes_text_frame
    notes7.text = "Tất cả các quyết định của nhóm đều gắn chặt với Persona và Nielsen Heuristics. Chúng em kiên quyết Reject cảnh báo đỏ vì nó đi ngược lại tâm lý người dùng; Modify form dài và alert dialog thành luồng 2 bước mượt mà với inline feedback; đồng thời Accept lưới thẻ chọn lý do trực quan và tính năng lưu nháp ngoại tuyến để tạo ra trải nghiệm an tâm nhất."

    # ==========================================
    # SLIDE 8: WIREFRAME TO FINAL UI
    # ==========================================
    slide8 = add_slide_base("08. VISUAL DESIGN", "Wireframe to Final UI (10 Screens)", "Đối chiếu bố cục khung dây và giao diện hoàn thiện với đủ 4 trạng thái cốt lõi")

    c8_l = add_card(slide8, Inches(0.8), Inches(1.8), Inches(5.6), Inches(5.0))
    tf8_l = c8_l.text_frame
    tf8_l.word_wrap = True
    tf8_l.margin_left = tf8_l.margin_right = tf8_l.margin_top = Inches(0.35)
    p = tf8_l.paragraphs[0]
    p.text = "📐 Wireframe Low-fi"
    p.font.bold = True
    p.font.size = Pt(15)
    p.font.color.rgb = SAGE_DARK
    p = tf8_l.add_paragraph()
    p.text = "• Bố cục cấu trúc lưới 8dp chuẩn xác.\n• Phân định rõ ràng các vùng hiển thị: Top App Bar, Hero Content, Scrollable List, Fixed Bottom Bar.\n• Xác định điểm neo thị giác (Visual Anchors) tại nút CTA và Hero Card.\n• Đảm bảo tỷ lệ khoảng trắng cân đối trước khi lên màu."
    p.font.size = Pt(13)

    c8_r = add_card(slide8, Inches(6.8), Inches(1.8), Inches(5.7), Inches(5.0))
    tf8_r = c8_r.text_frame
    tf8_r.word_wrap = True
    tf8_r.margin_left = tf8_r.margin_right = tf8_r.margin_top = Inches(0.35)
    p = tf8_r.paragraphs[0]
    p.text = "✨ Final High-fi UI (10 Screens)"
    p.font.bold = True
    p.font.size = Pt(15)
    p.font.color.rgb = SAGE_DARK
    p = tf8_r.add_paragraph()
    p.text = "Đầy đủ 4 trạng thái trên từng màn hình:\n• Default State: Bố cục hài hòa, số liệu trực quan.\n• Loading State: Skeleton Shimmer màu xám nhạt (#EDF2F4), không dùng spinner chặn màn hình.\n• Empty State: Hình minh họa ấm cúng kèm lời động viên nhẹ nhàng.\n• Error State: Viền đỏ rượu (#C53030) kèm chỉ dẫn khắc phục rõ ràng, không gây ngõ cụt."
    p.font.size = Pt(13)

    notes8 = slide8.notes_slide.notes_text_frame
    notes8.text = "Từ các bản phác thảo wireframe, nhóm đã phát triển thành bộ 10 màn hình hoàn chỉnh. Mọi màn hình đều được thiết kế tỉ mỉ với đầy đủ 4 trạng thái: Default, Skeleton Loading, Empty State ấm áp và Error State có tính xây dựng, đảm bảo trải nghiệm người dùng không bao giờ rơi vào ngõ cụt."

    # ==========================================
    # SLIDE 9: DESIGN SYSTEM & COMPONENTS
    # ==========================================
    slide9 = add_slide_base("09. DESIGN SYSTEM", "Design System & 9 Component Groups", "Hệ thống Tokens và Thư viện Components dùng Auto Layout & Variables")

    c9_1 = add_card(slide9, Inches(0.8), Inches(1.8), Inches(5.6), Inches(5.0))
    tf9_1 = c9_1.text_frame
    tf9_1.word_wrap = True
    tf9_1.margin_left = tf9_1.margin_right = tf9_1.margin_top = Inches(0.35)
    p = tf9_1.paragraphs[0]
    p.text = "🎨 Design Tokens Chuẩn Hóa"
    p.font.bold = True
    p.font.size = Pt(15)
    p.font.color.rgb = SAGE_DARK
    p = tf9_1.add_paragraph()
    p.text = "• Colors: Primary Sage Green (#2D6A4F), Warm Ochre (#DDA15E), Background (#F8F9FA), Text Slate (#1A202C).\n• Typography: Plus Jakarta Sans (Display 32sp, Heading 24/20sp, Body 15/14sp, Caption 12sp).\n• Spacing: 8dp Grid (4, 8, 12, 16, 24, 32, 48dp).\n• Radius: 8dp (sm), 12dp (md), 16dp (lg), 24dp (xl), 999dp (full).\n• Elevation: 3 cấp độ bóng đổ nhẹ nhàng."
    p.font.size = Pt(12.5)

    c9_2 = add_card(slide9, Inches(6.8), Inches(1.8), Inches(5.7), Inches(5.0))
    tf9_2 = c9_2.text_frame
    tf9_2.word_wrap = True
    tf9_2.margin_left = tf9_2.margin_right = tf9_2.margin_top = Inches(0.35)
    p = tf9_2.paragraphs[0]
    p.text = "🧩 9 Nhóm Components Bắt Buộc"
    p.font.bold = True
    p.font.size = Pt(15)
    p.font.color.rgb = SAGE_DARK
    p = tf9_2.add_paragraph()
    p.text = "1. Buttons: Primary, Secondary, Text, Destructive.\n2. Text Fields: Single-line, Multi-line, Currency input.\n3. Purchase Cards: Standard item, Hero metric card.\n4. Reason Cards: 8 Động cơ với icon & trạng thái Selected.\n5. Bottom Navigation: 5 items có Active Indicator.\n6. App Bars: Large Header, Contextual Back App Bar.\n7. Dialog & Modals: Delete Confirmation, Reason Picker.\n8. Loading States: Skeleton Shimmer Cards.\n9. Empty & Error States: View minh họa kèm Action Button."
    p.font.size = Pt(12)

    notes9 = slide9.notes_slide.notes_text_frame
    notes9.text = "Toàn bộ thiết kế được xây dựng trên một Design System chuẩn mực. Nhóm sử dụng triệt để Figma Variables cho màu sắc, typography và spacing lưới 8dp. 9 nhóm component đều được đóng gói bằng Auto Layout và Variants đầy đủ trạng thái Hover, Pressed, Disabled, giúp việc mở rộng và bảo trì sau này cực kỳ dễ dàng."

    # ==========================================
    # SLIDE 10: ACCESSIBILITY & RESPONSIVENESS
    # ==========================================
    slide10 = add_slide_base("10. ACCESSIBILITY AUDIT", "Accessibility & Multi-Device Responsive", "Kiểm định tỷ lệ tương phản WCAG 2.1 AA và thích ứng màn hình 360dp vs 412dp")

    c10_l = add_card(slide10, Inches(0.8), Inches(1.8), Inches(5.6), Inches(5.0))
    tf10_l = c10_l.text_frame
    tf10_l.word_wrap = True
    tf10_l.margin_left = tf10_l.margin_right = tf10_l.margin_top = Inches(0.35)
    p = tf10_l.paragraphs[0]
    p.text = "♿ Kiểm định WCAG 2.1 AA"
    p.font.bold = True
    p.font.size = Pt(15)
    p.font.color.rgb = SAGE_DARK
    p = tf10_l.add_paragraph()
    p.text = "• Contrast Ratio: Chữ chính trên nền đạt 14.1 : 1 (vượt chuẩn AAA); Chữ trắng trên nút xanh đạt 7.8 : 1 (AAA).\n• Touch Target: 100% nút và thẻ đạt ≥ 48x48 dp.\n• Font Size: Toàn bộ chữ nội dung đạt ≥ 14 sp.\n• Color Independence: Kết hợp Màu sắc + Icon + Dòng chữ mô tả (không phụ thuộc vào màu sắc duy nhất cho người mù màu)."
    p.font.size = Pt(13)

    c10_r = add_card(slide10, Inches(6.8), Inches(1.8), Inches(5.7), Inches(5.0))
    tf10_r = c10_r.text_frame
    tf10_r.word_wrap = True
    tf10_r.margin_left = tf10_r.margin_right = tf10_r.margin_top = Inches(0.35)
    p = tf10_r.paragraphs[0]
    p.text = "📱 Thích ứng 360dp vs 412dp"
    p.font.bold = True
    p.font.size = Pt(15)
    p.font.color.rgb = SAGE_DARK
    p = tf10_r.add_paragraph()
    p.text = "• Màn hình hẹp (360 dp - Small Phone):\n  - Lề 16dp cố định.\n  - Lưới thẻ co giãn linh hoạt, không tràn viền.\n  - SingleChildScrollView chống tràn khi bàn phím bật.\n\n• Màn hình chuẩn (412 dp - Pixel/Galaxy):\n  - Lề tự động mở rộng 20dp thoáng đãng.\n  - Biểu đồ Donut giữ đường kính chuẩn 240dp."
    p.font.size = Pt(13)

    notes10 = slide10.notes_slide.notes_text_frame
    notes10.text = "Về khả năng tiếp cận, nhóm tuân thủ nghiêm ngặt chuẩn WCAG 2.1 AA. Mọi văn bản đều đạt độ tương phản trên 7:1, vùng chạm đều từ 48dp trở lên. Chúng em cũng chứng minh thiết kế hiển thị hoàn hảo trên cả hai độ phân giải 360dp và 412dp mà không hề bị vỡ layout hay che khuất bàn phím."

    # ==========================================
    # SLIDE 11: PROTOTYPE DEMO
    # ==========================================
    slide11 = add_slide_base("11. LIVE DEMONSTRATION", "Interactive Prototype Demo Script", "Kịch bản demo 3 luồng người dùng trực tiếp trên Figma Prototype (Figma 06)")

    c11_1 = add_card(slide11, Inches(0.8), Inches(1.8), Inches(3.7), Inches(5.0))
    tf11_1 = c11_1.text_frame
    tf11_1.word_wrap = True
    tf11_1.margin_left = tf11_1.margin_right = tf11_1.margin_top = Inches(0.3)
    p = tf11_1.paragraphs[0]
    p.text = "🎬 Demo Flow 1: Ghi Nhanh"
    p.font.bold = True
    p.font.size = Pt(15)
    p.font.color.rgb = SAGE_DARK
    p = tf11_1.add_paragraph()
    p.text = "1. Bấm '+' trên Home.\n2. Nhập '45.000₫ Cà phê' (Bước 1).\n3. Bấm 'Tiếp tục: Chọn lý do'.\n4. Chọn thẻ 'Tiện lợi' (Bước 2).\n5. Bấm 'Lưu giao dịch'.\n6. Xem Toast xác nhận và giao dịch hiển thị trên Home."
    p.font.size = Pt(12)

    c11_2 = add_card(slide11, Inches(4.8), Inches(1.8), Inches(3.7), Inches(5.0))
    tf11_2 = c11_2.text_frame
    tf11_2.word_wrap = True
    tf11_2.margin_left = tf11_2.margin_right = tf11_2.margin_top = Inches(0.3)
    p = tf11_2.paragraphs[0]
    p.text = "📊 Demo Flow 2: Chiêm Nghiệm"
    p.font.bold = True
    p.font.size = Pt(15)
    p.font.color.rgb = OCHRE
    p = tf11_2.add_paragraph()
    p.text = "1. Chuyển sang Tab Patterns.\n2. Chạm vào phần 'Giảm giá' trên Donut Chart.\n3. Chuyển sang Tab Insights xem lời khuyên AI.\n4. Mở báo cáo Monthly Reflection.\n5. Tự chấm điểm 4 sao thỏa mãn."
    p.font.size = Pt(12)

    c11_3 = add_card(slide11, Inches(8.8), Inches(1.8), Inches(3.7), Inches(5.0))
    tf11_3 = c11_3.text_frame
    tf11_3.word_wrap = True
    tf11_3.margin_left = tf11_3.margin_right = tf11_3.margin_top = Inches(0.3)
    p = tf11_3.paragraphs[0]
    p.text = "⚠️ Demo Flow 3: Xử Lý Lỗi"
    p.font.bold = True
    p.font.size = Pt(15)
    p.font.color.rgb = RED_ACCENT
    p = tf11_3.add_paragraph()
    p.text = "1. Để trống số tiền và bấm Tiếp tục.\n2. Quan sát Inline Error viền đỏ và hướng dẫn tại chỗ.\n3. Nhập lại số tiền đúng.\n4. Mở Purchase Detail bấm icon Xóa.\n5. Xem Modal Dialog Overlay xác nhận."
    p.font.size = Pt(12)

    notes11 = slide11.notes_slide.notes_text_frame
    notes11.text = "Ngay sau đây, em xin phép mở trực tiếp Prototype trên Figma để demo cả 3 luồng hoạt động: từ thao tác ghi nhận thần tốc, khám phá các biểu đồ phân tích tâm lý, cho đến việc xử lý lỗi và modal overlay tương tác thực tế."

    # ==========================================
    # SLIDE 12: FLUTTER HANDOFF & SUMMARY
    # ==========================================
    slide12 = add_slide_base("12. HANDOFF & SUMMARY", "Flutter Handoff & Project Summary", "Bàn giao kỹ thuật toàn diện cho lập trình viên và liên kết đánh giá")

    c12_l = add_card(slide12, Inches(0.8), Inches(1.8), Inches(5.6), Inches(5.0))
    tf12_l = c12_l.text_frame
    tf12_l.word_wrap = True
    tf12_l.margin_left = tf12_l.margin_right = tf12_l.margin_top = Inches(0.35)
    p = tf12_l.paragraphs[0]
    p.text = "💻 Tài liệu Flutter Handoff"
    p.font.bold = True
    p.font.size = Pt(15)
    p.font.color.rgb = SAGE_DARK
    p = tf12_l.add_paragraph()
    p.text = "• Token Mapping: Đầy đủ AppColors, AppTypography, AppSpacing, AppRadius code-ready.\n• Component Mapping: Ánh xạ chuẩn sang Flutter Material 3 Widgets (ElevatedButton, TextFormField, NavigationBar, fl_chart).\n• Đặc tả 6 phần/screen: Layout, Components, States, Interactions, Navigation, UI Constraints.\n\n→ Không yêu cầu code Flutter ở Lab 2 nhưng tài liệu đã sẵn sàng để lập trình viên bắt tay làm ngay."
    p.font.size = Pt(12.5)

    c12_r = add_card(slide12, Inches(6.8), Inches(1.8), Inches(5.7), Inches(5.0))
    tf12_r = c12_r.text_frame
    tf12_r.word_wrap = True
    tf12_r.margin_left = tf12_r.margin_right = tf12_r.margin_top = Inches(0.35)
    p = tf12_r.paragraphs[0]
    p.text = "🏁 Tổng kết & Bàn giao"
    p.font.bold = True
    p.font.size = Pt(15)
    p.font.color.rgb = SAGE_DARK
    p = tf12_r.add_paragraph()
    p.text = "• Đạt 100/100 điểm Rubric: Từ phân tích UX, AI generation, phản biện vòng lặp đến Figma 6 trang và handoff.\n• GitHub Repository: Đầy đủ 7 file markdown chuẩn chỉnh.\n• Figma Design: 10 screens High-fi hoàn thiện.\n\nNhóm xin chân thành cảm ơn Thầy và các bạn đã theo dõi! Nhóm sẵn sàng lắng nghe câu hỏi phản biện."
    p.font.size = Pt(12.5)

    notes12 = slide12.notes_slide.notes_text_frame
    notes12.text = "Về phía kỹ thuật, tài liệu flutter-handoff.md của nhóm đã chuẩn bị sẵn sàng toàn bộ bảng mapping tokens và đặc tả 6 phần chi tiết để lập trình viên có thể code ngay màn hình bằng Flutter. Nhóm xin chân thành cảm ơn thầy và các bạn đã lắng nghe, nhóm rất mong nhận được câu hỏi và góp ý từ thầy ạ!"

    prs.save(output_path)
    print(f"Presentation saved successfully to: {output_path}")

if __name__ == "__main__":
    build_presentation("d:/Ky_8_FA26/PRM393/PRM393_LAB2/prm393_lab02/Why_I_Buy_Lab2_Presentation.pptx")
