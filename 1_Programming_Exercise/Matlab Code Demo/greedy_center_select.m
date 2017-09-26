function cent = greedy_center_select(x, k)
% *********************************************************************** %
% Greedy Algorithm for Center Slection Problem.
% --------
% INPUT  :
% --------
%   x    : matrix(point_num, dimension_num), Double
%          point set
%   k    : matrix(1, 1), Integer
%          total number of centers
% --------
% OUTPUT :
% --------
%   cent : matrix(k, dimension_num), Double
% --------
% Example:
% --------
%     %%
%     rng(0);
%     set = [mvnrnd([2 -2], [2 1.5; 1.5, 2], 500); mvnrnd([-2 2], [2 1.5; 1.5, 2], 500)];
%     plot(set(:, 1), set(:, 2), '.'); hold on;
%     cent = greedy_center_select(set, 6);
%     for cent_ind = 1 : size(cent)
%         text(cent(cent_ind, 1), cent(cent_ind, 2), num2str(cent_ind), 'Color', 'r', 'FontSize', 25);
%         hold on;
%     end
%     hold off;
% 
%     %%
%     set = [(-10 : 10)' (-10 : 10)'];
%     plot(set(:, 1), set(:, 2), '.'); hold on;
%     cent = greedy_center_select(set, 5);
%     for cent_ind = 1 : size(cent)
%         text(cent(cent_ind, 1), cent(cent_ind, 2), num2str(cent_ind), 'Color', 'r', 'FontSize', 25);
%         hold on;
%     end
%     hold off;
% *********************************************************************** %
    cent = x(1, :);
    x(1, :) = [];
    for i = 2 : k
        dist = pdist2(x, cent);
        min_dist = min(dist, [], 2);
        [~, max_min_dist]= max(min_dist);
        cent = cat(1, cent, x(max_min_dist, :));
        x(max_min_dist, :) = [];
    end
end
