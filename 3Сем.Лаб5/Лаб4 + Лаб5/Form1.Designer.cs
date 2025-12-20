namespace Лаб4_Рахманов
{
    partial class Form1
    {
        /// <summary>
        ///  Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        ///  Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        ///  Required method for Designer support - do not modify
        ///  the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            btnLoadFile = new Button();
            btnSearch = new Button();
            txtSearch = new TextBox();
            lstResults = new ListBox();
            lblTime = new Label();
            lblWordCount = new Label();
            SuspendLayout();
            // 
            // btnLoadFile
            // 
            btnLoadFile.Location = new Point(41, 29);
            btnLoadFile.Name = "btnLoadFile";
            btnLoadFile.Size = new Size(237, 126);
            btnLoadFile.TabIndex = 0;
            btnLoadFile.Text = "Загрузить файл";
            btnLoadFile.UseVisualStyleBackColor = true;
            btnLoadFile.Click += btnLoadFile_Click;
            // 
            // btnSearch
            // 
            btnSearch.Location = new Point(463, 353);
            btnSearch.Name = "btnSearch";
            btnSearch.Size = new Size(196, 40);
            btnSearch.TabIndex = 1;
            btnSearch.Text = "Найти";
            btnSearch.UseVisualStyleBackColor = true;
            btnSearch.Click += btnSearch_Click;
            // 
            // txtSearch
            // 
            txtSearch.Location = new Point(41, 360);
            txtSearch.Name = "txtSearch";
            txtSearch.Size = new Size(402, 27);
            txtSearch.TabIndex = 2;
            // 
            // lstResults
            // 
            lstResults.FormattingEnabled = true;
            lstResults.Location = new Point(687, 29);
            lstResults.Name = "lstResults";
            lstResults.Size = new Size(402, 364);
            lstResults.TabIndex = 3;
            // 
            // lblTime
            // 
            lblTime.AutoSize = true;
            lblTime.Location = new Point(41, 197);
            lblTime.Name = "lblTime";
            lblTime.Size = new Size(121, 20);
            lblTime.TabIndex = 4;
            lblTime.Text = "Время загрузки:";
            // 
            // lblWordCount
            // 
            lblWordCount.AutoSize = true;
            lblWordCount.Location = new Point(41, 286);
            lblWordCount.Name = "lblWordCount";
            lblWordCount.Size = new Size(133, 20);
            lblWordCount.TabIndex = 5;
            lblWordCount.Text = "Уникальных слов:";
            // 
            // Form1
            // 
            AutoScaleDimensions = new SizeF(8F, 20F);
            AutoScaleMode = AutoScaleMode.Font;
            ClientSize = new Size(1219, 450);
            Controls.Add(lblWordCount);
            Controls.Add(lblTime);
            Controls.Add(lstResults);
            Controls.Add(txtSearch);
            Controls.Add(btnSearch);
            Controls.Add(btnLoadFile);
            Name = "Form1";
            Text = "Form1";
            ResumeLayout(false);
            PerformLayout();
        }

        #endregion

        private Button btnLoadFile;
        private Button btnSearch;
        private TextBox txtSearch;
        private ListBox lstResults;
        private Label lblTime;
        private Label lblWordCount;
    }
}
