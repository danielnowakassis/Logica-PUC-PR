from manimlib import *

class biimplicacao(Scene):
    def construct(self):
        table = r"""
        \begin{table}[]
        \centering
        \begin{tabular}{|l|l|l|}\hline
        T & F & n(p v q) \\\hline
        &  &    \\\hline
        &  &   \\\hline
        &  &      \\\hline    
        &  &      \\\hline
        \end{tabular}
        \end{table}
        """
        tex_table = TexText(table)
        tex_table. move_to([-4.5,0,0])
        p = Tex("p")
        q = Tex("q")
        pq = Tex("p \\Leftrightarrow q", color = GREEN_SCREEN)
        p.move_to([-6.2,1.2,0])
        q.move_to([-5.2,1.2,0])
        pq.move_to([-3.7,1.2,0])
        self.play(Write(tex_table),  Write(p), Write(q), Write(pq), run_time = 3)
        self.wait(9)
        pqex = Tex("p \\Leftrightarrow q \\equiv")
        pqvfex = Tex("(p \\Rightarrow q) \\land (q \\Rightarrow p)")
        pqex.move_to([-1,-0.1,0])
        pqvfex.move_to([2,0,0])
        self.play(Write(pqex))
        self.wait(2)
        self.play(Write(pqvfex))
        self.wait(2)
        self.wait(10)
        self.wait(6)
        vv1 = Text("(V → V) ^ (V → V)",font_size =30, t2c = {"V" : BLUE, "F": RED_E})
        vv2 = Text("(V ^ V)",font_size =30, t2c = {"V" : BLUE, "F": RED_E})
        vv3 = Text("(V)",font_size =30, t2c = {"V" : BLUE, "F": RED_E})
        vv1.move_to([2,0,0])
        vv2.move_to([2,0,0])
        vv3.move_to([2,0,0])
        self.play(ReplacementTransform(pqvfex,vv1))
        self.wait(2)
        self.play(ReplacementTransform(vv1, vv2))
        self.wait(2)

        pv1 = Tex("V", color= BLUE)
        pv2 = Tex("V", color= BLUE)
        pf1 = Tex("F", color= RED)
        pf2 = Tex("F", color= RED)
        #
        pv1.move_to([-6.2,0.6,0])
        pv2.move_to([-6.2,0,0])
        pf1.move_to([-6.2,-0.6,0])
        pf2.move_to([-6.2,-1.2,0])
        #
        qv1 = Tex("V", color= BLUE)
        qf1 = Tex("F", color= RED)
        qv2 = Tex("V", color= BLUE)
        qf2 = Tex("F", color= RED)
        #
        qv1.move_to([-5.2,0.6,0])
        qf1.move_to([-5.2,0,0])
        qv2.move_to([-5.2,-0.6,0])
        qf2.move_to([-5.2,-1.2,0])
        #
        pqv1 = Tex("V", color= BLUE)
        pqf1 = Tex("F", color= RED)
        pqf2 = Tex("F", color= RED)
        pqv2 = Tex("V", color= BLUE)
        #
        pqv1.move_to([-3.7,0.6,0])
        pqf1.move_to([-3.7,0,0])
        pqf2.move_to([-3.7,-0.6,0])
        pqv2.move_to([-3.7,-1.2,0])

        self.play(FadeTransform(vv2, vv3),Write(pv1), Write(qv1), Write(pqv1))
        self.wait(3)
        ff1 = Text("(F → F) ^ (F → F)",font_size =30, t2c = {"V" : BLUE, "F": RED_E})
        ff2 = Text("(V ^ V)",font_size =30, t2c = {"V" : BLUE, "F": RED_E})
        ff3 = Text("(V)",font_size =30, t2c = {"V" : BLUE, "F": RED_E})
        ff1.move_to([2,0,0])
        ff2.move_to([2,0,0])
        ff3.move_to([2,0,0])
        self.play(FadeTransform(vv3, ff1))
        self.wait(4)
        self.play(FadeTransform(ff1, ff2))
        self.wait(2)
        self.play(FadeTransform(ff2, ff3),Write(pf2), Write(qf2), Write(pqv2))
        self.wait(5)
        vf1 = Text("(V → F) ^ (F → V)",font_size =30, t2c = {"V" : BLUE, "F": RED_E})
        vf2 = Text("(F ^ V)",font_size =30, t2c = {"V" : BLUE, "F": RED_E})
        vf3 = Text("(F)",font_size =30, t2c = {"V" : BLUE, "F": RED_E})
        vf1.move_to([2,0,0])
        vf2.move_to([2,0,0])
        vf3.move_to([2,0,0])
        self.play(FadeTransform(ff3, vf1))
        self.wait(5)
        self.play(FadeTransform(vf1, vf2))
        self.wait(3)
        self.play(FadeTransform(vf2, vf3),Write(pv2), Write(qf1), Write(pqf1),Write(pf1), Write(qv2), Write(pqf2))
        self.wait(5)